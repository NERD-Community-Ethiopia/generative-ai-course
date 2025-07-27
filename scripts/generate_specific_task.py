#!/usr/bin/env python3
"""
Script to create a specific GitHub issue for a given assignee, with due date, tags, and an optional comment.
"""
import argparse
import sys
from datetime import datetime
from github import Github, GithubException
import requests

# TODO: Set this to your GitHub Project (beta/v2) node_id
PROJECT_NODE_ID = "<YOUR_PROJECT_NODE_ID>"

def add_issue_to_project(issue_node_id, project_node_id, github_token):
    query = """
    mutation {
      addProjectV2ItemById(input: {projectId: \"%s\", contentId: \"%s\"}) {
        item { id }
      }
    }
    """ % (project_node_id, issue_node_id)
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query},
        headers=headers
    )
    print("Add to project response:", response.json())

def main():
    parser = argparse.ArgumentParser(description="Create a specific GitHub issue for an assignee with due date, tags, and comment.")
    parser.add_argument("--title", required=True, help="Issue title")
    parser.add_argument("--body", required=True, help="Issue body/description")
    parser.add_argument("--assignee", required=True, help="GitHub username to assign the issue to")
    parser.add_argument("--due-date", required=False, help="Due date (YYYY-MM-DD), will create/find a milestone")
    parser.add_argument("--labels", required=False, nargs="*", default=[], help="Labels/tags for the issue (space separated)")
    parser.add_argument("--comment", required=False, help="Optional comment to add after issue creation")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--repo", default="NERD-Community-Ethiopia/generative-ai-course", help="Repository name (owner/repo)")
    args = parser.parse_args()

    g = Github(args.token)
    repo = g.get_repo(args.repo)

    # Handle milestone (due date)
    milestone_number = None
    if args.due_date:
        milestone_title = f"Due {args.due_date}"
        # Try to find existing milestone
        for m in repo.get_milestones(state='open'):
            if m.title == milestone_title:
                milestone_number = m.number
                break
        if milestone_number is None:
            # Create new milestone
            try:
                due_on = datetime.strptime(args.due_date, "%Y-%m-%d")
                milestone = repo.create_milestone(title=milestone_title, due_on=due_on)
                milestone_number = milestone.number
                print(f"Created milestone: {milestone_title}")
            except GithubException as e:
                print(f"Error creating milestone: {e}")
                sys.exit(1)

    # Create the issue
    try:
        issue = repo.create_issue(
            title=args.title,
            body=args.body,
            assignees=[args.assignee],
            labels=args.labels,
            milestone=milestone_number
        )
        print(f"Created issue: {issue.title} (#{issue.number}) assigned to {args.assignee}")
        # Add the created issue to the GitHub Project (beta/v2)
        add_issue_to_project(issue.node_id, PROJECT_NODE_ID, g._Github__requester._Authorization__token)
    except GithubException as e:
        print(f"Error creating issue: {e}")
        sys.exit(1)

    # Add a comment if specified
    if args.comment:
        try:
            issue.create_comment(args.comment)
            print("Added comment to issue.")
        except GithubException as e:
            print(f"Error adding comment: {e}")

if __name__ == "__main__":
    main() 