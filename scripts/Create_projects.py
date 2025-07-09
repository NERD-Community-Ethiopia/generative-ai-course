#!/usr/bin/env python3
"""
Create a new GitHub Project (beta) in the organization using the GraphQL API and add all issues for a given week (milestone) to the board.
Usage:
  python scripts/create_project_beta.py --token YOUR_TOKEN --org ORG_NAME --repo REPO_NAME --name "Sprint: Week 1" --week 1
"""
import argparse
import requests
import sys
from github import Github

def get_org_id(token, org):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    org_query = """
    query($login: String!) {
      organization(login: $login) {
        id
      }
    }
    """
    org_vars = {"login": org}
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": org_query, "variables": org_vars},
        headers=headers
    )
    if resp.status_code != 200 or "errors" in resp.json():
        print(f"Error fetching org ID: {resp.text}")
        sys.exit(1)
    return resp.json()["data"]["organization"]["id"]

def create_project(token, org_id, name):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    query = """
    mutation($org: ID!, $name: String!) {
      createProjectV2(input: {ownerId: $org, title: $name}) {
        projectV2 {
          id
          title
          url
        }
      }
    }
    """
    variables = {
        "org": org_id,
        "name": name
    }
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers
    )
    if resp.status_code != 200 or "errors" in resp.json():
        print(f"Error creating project: {resp.text}")
        sys.exit(1)
    project = resp.json()["data"]["createProjectV2"]["projectV2"]
    print(f"Created Project: {project['title']}")
    print(f"URL: {project['url']}")
    return project["id"], project["title"]

def get_issues_for_week(token, repo_name, week):
    g = Github(token)
    repo = g.get_repo(repo_name)
    milestone_title = f"Week {week}"
    issues = [issue for issue in repo.get_issues(state='open')
              if issue.milestone and issue.milestone.title == milestone_title]
    return issues

def add_issue_to_project(token, project_id, issue_node_id):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    mutation = """
    mutation($project: ID!, $contentId: ID!) {
      addProjectV2ItemById(input: {projectId: $project, contentId: $contentId}) {
        item {
          id
        }
      }
    }
    """
    variables = {"project": project_id, "contentId": issue_node_id}
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": mutation, "variables": variables},
        headers=headers
    )
    if resp.status_code != 200 or "errors" in resp.json():
        print(f"Error adding issue to project: {resp.text}")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Create a new GitHub Project (beta) in the organization using GraphQL API and add all issues for a week.")
    parser.add_argument("--token", required=True, help="GitHub token with project and repo scopes")
    parser.add_argument("--org", required=True, help="GitHub organization name")
    parser.add_argument("--repo", required=True, help="GitHub repository name (owner/repo)")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--week", required=True, help="Week number (milestone title)")
    args = parser.parse_args()

    org_id = get_org_id(args.token, args.org)
    project_id, project_title = create_project(args.token, org_id, args.name)
    issues = get_issues_for_week(args.token, args.repo, args.week)
    print(f"Found {len(issues)} issues for Week {args.week}")
    for issue in issues:
        print(f"Adding issue: {issue.title}")
        success = add_issue_to_project(args.token, project_id, issue.node_id)
        if success:
            print(f"  Added: {issue.title}")
        else:
            print(f"  Failed to add: {issue.title}")

if __name__ == "__main__":
    main() 
