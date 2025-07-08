#!/usr/bin/env python3
"""
Create a new GitHub Project (beta) in the organization using the GraphQL API.
Usage:
  python scripts/create_project_beta.py --token YOUR_TOKEN --org ORG_NAME --name "Project Name" --description "Project description"
"""
import argparse
import requests
import sys

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

def main():
    parser = argparse.ArgumentParser(description="Create a new GitHub Project (beta) in the organization using GraphQL API.")
    parser.add_argument("--token", required=True, help="GitHub token with project and repo scopes")
    parser.add_argument("--org", required=True, help="GitHub organization name")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--description", default="", help="Project description")
    args = parser.parse_args()

    org_id = get_org_id(args.token, args.org)
    create_project(args.token, org_id, args.name)

if __name__ == "__main__":
    main() 