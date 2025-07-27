#!/usr/bin/env python3
"""
Automated Task Generation Script

This script generates GitHub issues for weekly tasks based on the course structure.
It creates tasks for lectures, workshops, assignments, and documentation.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests

try:
    from github import Github, GithubException
except ImportError:
    print("Error: PyGithub not installed. Run: pip install PyGithub")
    sys.exit(1)

# TODO: Set this to your GitHub Project (beta/v2) node_id
PROJECT_NODE_ID = "<YOUR_PROJECT_NODE_ID>"

# Set course start date from env or default
COURSE_START_DATE_STR = os.getenv("COURSE_START_DATE", "2024-07-01")  # YYYY-MM-DD
COURSE_START_DATE = datetime.strptime(COURSE_START_DATE_STR, "%Y-%m-%d")

def get_current_week(start_date):
    today = datetime.now()
    delta = today - start_date
    week = delta.days // 7 + 1
    return min(max(week, 1), 8)  # Clamp between 1 and 8

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

class TaskGenerator:
    def __init__(self, token: str, repo_name: str = "NERD-Community-Ethiopia/generative-ai-course"):
        self.github = Github(token)
        self.repo = self.github.get_repo(repo_name)
        self.week_templates = self._load_week_templates()
    
    def _load_week_templates(self) -> Dict:
        """Load task templates for each week"""
        return {
            "1": {
                "title": "Week 1: Introduction to Python and AI",
                "tasks": [
                    {
                        "title": "Create Week 1 Lecture Materials",
                        "body": "Develop comprehensive lecture materials for Week 1 covering:\n- Python basics for AI\n- Introduction to generative AI\n- Setting up development environment\n- Basic text processing",
                        "labels": ["lecture", "week-1", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 1"
                    },
                    {
                        "title": "Design Week 1 Workshop Exercises",
                        "body": "Create hands-on workshop exercises for Week 1:\n- Python fundamentals practice\n- Simple text processing tasks\n- Basic AI concept exploration\n- Environment setup verification",
                        "labels": ["workshop", "week-1", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 1"
                    },
                    {
                        "title": "Create Week 1 Assignment",
                        "body": "Design student assignment for Week 1:\n- Text preprocessing challenge\n- Simple sentiment analysis\n- File I/O operations\n- Basic AI application",
                        "labels": ["assignment", "week-1", "medium-priority"],
                        "assignees": [],
                        "milestone": "Week 1"
                    },
                    {
                        "title": "Update Week 1 Documentation",
                        "body": "Update and improve Week 1 documentation:\n- README.md updates\n- Setup instructions\n- Troubleshooting guide\n- Learning resources",
                        "labels": ["documentation", "week-1", "low-priority"],
                        "assignees": [],
                        "milestone": "Week 1"
                    }
                ]
            },
            "2": {
                "title": "Week 2: Neural Networks Fundamentals",
                "tasks": [
                    {
                        "title": "Create Week 2 Lecture Materials",
                        "body": "Develop lecture materials for Week 2 covering:\n- Neural network basics\n- Perceptrons and activation functions\n- Backpropagation\n- Simple neural network implementation",
                        "labels": ["lecture", "week-2", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 2"
                    },
                    {
                        "title": "Design Week 2 Workshop Exercises",
                        "body": "Create workshop exercises for Week 2:\n- Building simple neural networks\n- Training and testing models\n- Visualization of learning process\n- Performance analysis",
                        "labels": ["workshop", "week-2", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 2"
                    },
                    {
                        "title": "Create Week 2 Assignment",
                        "body": "Design assignment for Week 2:\n- Neural network from scratch\n- Classification problem\n- Model evaluation\n- Performance optimization",
                        "labels": ["assignment", "week-2", "medium-priority"],
                        "assignees": [],
                        "milestone": "Week 2"
                    }
                ]
            },
            "3": {
                "title": "Week 3: Deep Learning with PyTorch",
                "tasks": [
                    {
                        "title": "Create Week 3 Lecture Materials",
                        "body": "Develop lecture materials for Week 3 covering:\n- PyTorch fundamentals\n- Tensors and operations\n- Neural network modules\n- Training loops",
                        "labels": ["lecture", "week-3", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 3"
                    },
                    {
                        "title": "Design Week 3 Workshop Exercises",
                        "body": "Create workshop exercises for Week 3:\n- PyTorch tensor operations\n- Building neural networks\n- Training and validation\n- Model saving and loading",
                        "labels": ["workshop", "week-3", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 3"
                    }
                ]
            },
            "4": {
                "title": "Week 4: Natural Language Processing",
                "tasks": [
                    {
                        "title": "Create Week 4 Lecture Materials",
                        "body": "Develop lecture materials for Week 4 covering:\n- NLP fundamentals\n- Text preprocessing\n- Word embeddings\n- Sequence models",
                        "labels": ["lecture", "week-4", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 4"
                    },
                    {
                        "title": "Design Week 4 Workshop Exercises",
                        "body": "Create workshop exercises for Week 4:\n- Text preprocessing pipeline\n- Word embedding visualization\n- Simple language models\n- Text classification",
                        "labels": ["workshop", "week-4", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 4"
                    }
                ]
            },
            "5": {
                "title": "Week 5: Large Language Models",
                "tasks": [
                    {
                        "title": "Create Week 5 Lecture Materials",
                        "body": "Develop lecture materials for Week 5 covering:\n- Transformer architecture\n- Attention mechanisms\n- Pre-trained models\n- Fine-tuning techniques",
                        "labels": ["lecture", "week-5", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 5"
                    },
                    {
                        "title": "Design Week 5 Workshop Exercises",
                        "body": "Create workshop exercises for Week 5:\n- Using pre-trained models\n- Fine-tuning for specific tasks\n- Prompt engineering\n- Model evaluation",
                        "labels": ["workshop", "week-5", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 5"
                    }
                ]
            },
            "6": {
                "title": "Week 6: Frontend Development for AI",
                "tasks": [
                    {
                        "title": "Create Week 6 Lecture Materials",
                        "body": "Develop lecture materials for Week 6 covering:\n- Frontend frameworks\n- API integration\n- Real-time updates\n- User experience design",
                        "labels": ["lecture", "week-6", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 6"
                    },
                    {
                        "title": "Design Week 6 Workshop Exercises",
                        "body": "Create workshop exercises for Week 6:\n- Building AI-powered UI\n- API integration\n- Real-time features\n- Responsive design",
                        "labels": ["workshop", "week-6", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 6"
                    }
                ]
            },
            "7": {
                "title": "Week 7: Automation & CI/CD",
                "tasks": [
                    {
                        "title": "Create Week 7 Lecture Materials",
                        "body": "Develop lecture materials for Week 7 covering:\n- CI/CD pipelines\n- GitHub Actions\n- Automated testing\n- Deployment strategies",
                        "labels": ["lecture", "week-7", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 7"
                    },
                    {
                        "title": "Design Week 7 Workshop Exercises",
                        "body": "Create workshop exercises for Week 7:\n- Setting up CI/CD\n- Writing automated tests\n- Security scanning\n- Deployment automation",
                        "labels": ["workshop", "week-7", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 7"
                    }
                ]
            },
            "8": {
                "title": "Week 8: Capstone Project",
                "tasks": [
                    {
                        "title": "Create Week 8 Lecture Materials",
                        "body": "Develop lecture materials for Week 8 covering:\n- Project planning\n- Architecture design\n- Integration strategies\n- Presentation preparation",
                        "labels": ["lecture", "week-8", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 8"
                    },
                    {
                        "title": "Design Week 8 Workshop Exercises",
                        "body": "Create workshop exercises for Week 8:\n- Project setup and planning\n- Architecture implementation\n- Integration testing\n- Demo preparation",
                        "labels": ["workshop", "week-8", "high-priority"],
                        "assignees": [],
                        "milestone": "Week 8"
                    }
                ]
            }
        }
    
    def create_milestone(self, week: str) -> Optional[int]:
        """Create milestone for the week if it doesn't exist"""
        milestone_title = f"Week {week}"
        
        # Check if milestone already exists
        for milestone in self.repo.get_milestones(state='open'):
            if milestone.title == milestone_title:
                return milestone.number
        
        # Create new milestone
        try:
            due_date = datetime.now() + timedelta(weeks=int(week))
            milestone = self.repo.create_milestone(
                title=milestone_title,
                description=f"Tasks for Week {week} of the Generative AI Course",
                due_on=due_date
            )
            print(f"Created milestone: {milestone_title}")
            return milestone.number
        except GithubException as e:
            print(f"Error creating milestone: {e}")
            return None
    
    def create_labels(self):
        """Create labels if they don't exist"""
        labels_to_create = [
            {"name": "lecture", "color": "0366d6", "description": "Lecture materials"},
            {"name": "workshop", "color": "28a745", "description": "Workshop exercises"},
            {"name": "assignment", "color": "ffa500", "description": "Student assignments"},
            {"name": "documentation", "color": "0075ca", "description": "Documentation updates"},
            {"name": "high-priority", "color": "d73a4a", "description": "High priority tasks"},
            {"name": "medium-priority", "color": "fbca04", "description": "Medium priority tasks"},
            {"name": "low-priority", "color": "0e8a16", "description": "Low priority tasks"},
            {"name": "bug", "color": "d73a4a", "description": "Something isn't working"},
            {"name": "enhancement", "color": "a2eeef", "description": "New feature or request"},
            {"name": "good first issue", "color": "7057ff", "description": "Good for newcomers"},
            {"name": "help wanted", "color": "008672", "description": "Extra attention is needed"},
        ]
        
        existing_labels = {label.name for label in self.repo.get_labels()}
        
        for label in labels_to_create:
            if label["name"] not in existing_labels:
                try:
                    self.repo.create_label(**label)
                    print(f"Created label: {label['name']}")
                except GithubException as e:
                    print(f"Error creating label {label['name']}: {e}")
    
    def generate_tasks(self, week: str, task_type: str = "all"):
        """Generate tasks for the specified week"""
        if week not in self.week_templates:
            print(f"Error: No template found for week {week}")
            return
        
        # Create milestone
        milestone_number = self.create_milestone(week)
        
        # Create labels
        self.create_labels()
        
        # Get tasks for the week
        week_data = self.week_templates[week]
        tasks = week_data["tasks"]
        
        # Filter tasks by type if specified
        if task_type != "all":
            tasks = [task for task in tasks if task_type in task["labels"]]
        
        created_issues = []
        
        for task in tasks:
            try:
                # Create issue
                issue = self.repo.create_issue(
                    title=task["title"],
                    body=task["body"],
                    labels=task["labels"],
                    assignees=task["assignees"],
                    milestone=milestone_number
                )
                # Add the created issue to the GitHub Project (beta/v2)
                add_issue_to_project(issue.node_id, PROJECT_NODE_ID, self.github._Github__requester._Authorization__token)
                created_issues.append(issue)
                print(f"Created issue: {issue.title} (#{issue.number})")
                
            except GithubException as e:
                print(f"Error creating issue '{task['title']}': {e}")
        
        print(f"\nCreated {len(created_issues)} issues for Week {week}")
        return created_issues


def main():
    parser = argparse.ArgumentParser(description="Generate GitHub issues for weekly tasks")
    parser.add_argument("--week", required=False, help="Week number (1-8). If not set, auto-calculated from course start date.")
    parser.add_argument("--type", default="all", choices=["all", "lecture", "workshop", "assignment", "documentation"],
                       help="Type of tasks to generate")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--repo", default="NERD-Community-Ethiopia/generative-ai-course",
                       help="Repository name (owner/repo)")
    
    args = parser.parse_args()
    
    # Determine week number
    if args.week is not None:
        week = args.week
    else:
        week = str(get_current_week(COURSE_START_DATE))
        print(f"Auto-calculated week: {week} (using course start date {COURSE_START_DATE.date()})")
    
    # Validate week number
    if not week.isdigit() or int(week) < 1 or int(week) > 8:
        print("Error: Week number must be between 1 and 8")
        sys.exit(1)
    
    # Create task generator
    generator = TaskGenerator(args.token, args.repo)
    
    # Generate tasks
    generator.generate_tasks(week, args.type)


if __name__ == "__main__":
    main() 