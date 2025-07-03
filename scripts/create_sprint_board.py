#!/usr/bin/env python3
"""
Sprint Board Creation Script

This script creates GitHub Projects boards for sprint management and
organizes issues into sprints.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional

try:
    from github import Github, GithubException
except ImportError:
    print("Error: PyGithub not installed. Run: pip install PyGithub")
    sys.exit(1)


class SprintBoardCreator:
    def __init__(self, token: str, repo_name: str = "NERD-Community-Ethiopia/generative-ai-course"):
        self.github = Github(token)
        self.repo = self.github.get_repo(repo_name)
        self.organization = self.github.get_organization("NERD-Community-Ethiopia")
    
    def create_sprint_board(self, sprint_name: str, start_date: str, end_date: str):
        """Create a new sprint board"""
        try:
            # Create project board
            project = self.organization.create_project(
                name=f"Sprint: {sprint_name}",
                body=f"Agile sprint board for {sprint_name}",
                state="open"
            )
            
            print(f"Created project board: {project.name}")
            
            # Create columns
            columns = [
                {"name": "Backlog", "position": 1},
                {"name": "To Do", "position": 2},
                {"name": "In Progress", "position": 3},
                {"name": "Review", "position": 4},
                {"name": "Done", "position": 5}
            ]
            
            for column in columns:
                project.create_column(name=column["name"])
                print(f"Created column: {column['name']}")
            
            # Get issues for this sprint
            sprint_issues = self.get_sprint_issues(sprint_name)
            
            # Add issues to backlog
            if sprint_issues:
                backlog_column = project.get_columns()[0]  # First column is backlog
                
                for issue in sprint_issues:
                    try:
                        backlog_column.create_card(content_id=issue.id, content_type="Issue")
                        print(f"Added issue to backlog: {issue.title}")
                    except GithubException as e:
                        print(f"Error adding issue to board: {e}")
            
            return project
            
        except GithubException as e:
            print(f"Error creating sprint board: {e}")
            return None
    
    def get_sprint_issues(self, sprint_name: str) -> List:
        """Get issues that belong to this sprint"""
        issues = []
        
        # Look for issues with sprint-related labels or milestones
        for issue in self.repo.get_issues(state='open'):
            # Check labels
            issue_labels = [label.name.lower() for label in issue.labels]
            
            # Check if issue belongs to this sprint
            if (sprint_name.lower() in issue_labels or
                sprint_name.lower() in issue.title.lower() or
                (issue.milestone and sprint_name.lower() in issue.milestone.title.lower())):
                issues.append(issue)
        
        return issues
    
    def create_weekly_sprint(self, week_number: int):
        """Create a weekly sprint board"""
        start_date = datetime.now() + timedelta(weeks=week_number-1)
        end_date = start_date + timedelta(days=6)
        
        sprint_name = f"Week {week_number}"
        
        return self.create_sprint_board(
            sprint_name=sprint_name,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d")
        )
    
    def list_existing_boards(self):
        """List all existing project boards"""
        try:
            projects = self.organization.get_projects()
            
            print("Existing project boards:")
            print("=" * 40)
            
            for project in projects:
                print(f"- {project.name} (ID: {project.id})")
                print(f"  State: {project.state}")
                print(f"  Created: {project.created_at}")
                print()
                
        except GithubException as e:
            print(f"Error listing projects: {e}")
    
    def update_board_automation(self, project_id: int):
        """Set up automation rules for the board"""
        # Note: GitHub Projects automation is currently in beta
        # This is a placeholder for future automation features
        print("Board automation setup (GitHub Projects automation is in beta)")
        print("Manual automation rules to consider:")
        print("- Move issues to 'In Progress' when assigned")
        print("- Move issues to 'Review' when PR is created")
        print("- Move issues to 'Done' when PR is merged")
        print("- Auto-assign reviewers based on labels")


def main():
    parser = argparse.ArgumentParser(description="Create GitHub Projects sprint boards")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--repo", default="NERD-Community-Ethiopia/generative-ai-course",
                       help="Repository name (owner/repo)")
    parser.add_argument("--sprint-name", help="Name of the sprint")
    parser.add_argument("--start-date", help="Sprint start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="Sprint end date (YYYY-MM-DD)")
    parser.add_argument("--week", type=int, help="Week number for weekly sprint")
    parser.add_argument("--list-boards", action="store_true", help="List existing boards")
    
    args = parser.parse_args()
    
    # Create board creator
    creator = SprintBoardCreator(args.token, args.repo)
    
    if args.list_boards:
        creator.list_existing_boards()
    elif args.week:
        creator.create_weekly_sprint(args.week)
    elif args.sprint_name and args.start_date and args.end_date:
        creator.create_sprint_board(args.sprint_name, args.start_date, args.end_date)
    else:
        print("Please specify either --week, --sprint-name with dates, or --list-boards")


if __name__ == "__main__":
    main() 