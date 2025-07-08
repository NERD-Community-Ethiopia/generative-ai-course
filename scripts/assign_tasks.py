#!/usr/bin/env python3
"""
Automated Task Assignment Script

This script automatically assigns GitHub issues to interns based on their
availability, skills, and current workload.
"""

import argparse
import json
import sys
from typing import Dict, List, Optional
from collections import defaultdict

try:
    from github import Github, GithubException
except ImportError:
    print("Error: PyGithub not installed. Run: pip install PyGithub")
    sys.exit(1)


class TaskAssigner:
    def __init__(self, token: str, repo_name: str = "NERD-Community-Ethiopia/generative-ai-course"):
        self.github = Github(token)
        self.repo = self.github.get_repo(repo_name)
        self.interns = self._load_interns()
    
    def _load_interns(self) -> Dict:
        """Load intern information and preferences"""
        return {
            "intern1": {
                "username": "intern1",  # Replace with actual usernames
                "name": "Intern One",
                "skills": ["python", "ai", "lectures"],
                "preferences": ["lecture", "documentation"],
                "max_tasks": 3,
                "current_tasks": 0
            },
            "intern2": {
                "username": "intern2",  # Replace with actual usernames
                "name": "Intern Two",
                "skills": ["python", "workshops", "testing"],
                "preferences": ["workshop", "assignment"],
                "max_tasks": 3,
                "current_tasks": 0
            },
            "intern3": {
                "username": "intern3",  # Replace with actual usernames
                "name": "Intern Three",
                "skills": ["python", "ci-cd", "security"],
                "preferences": ["documentation", "enhancement"],
                "max_tasks": 2,
                "current_tasks": 0
            }
        }
    
    def get_unassigned_issues(self) -> List:
        """Get all unassigned issues"""
        issues = []
        for issue in self.repo.get_issues(state='open'):
            if not issue.assignees and not issue.pull_request:
                issues.append(issue)
        return issues
    
    def get_intern_workload(self) -> Dict:
        """Calculate current workload for each intern"""
        workload = defaultdict(int)
        
        for issue in self.repo.get_issues(state='open'):
            for assignee in issue.assignees:
                workload[assignee.login] += 1
        
        return dict(workload)
    
    def calculate_task_score(self, issue, intern: Dict) -> float:
        """Calculate how well a task matches an intern's skills and preferences"""
        score = 0.0
        
        # Check skill matches
        issue_labels = [label.name.lower() for label in issue.labels]
        issue_body = issue.body.lower() if issue.body else ""
        
        # Skill matching
        for skill in intern["skills"]:
            if skill in issue_body or skill in issue_labels:
                score += 2.0
        
        # Preference matching
        for preference in intern["preferences"]:
            if preference in issue_labels:
                score += 1.5
        
        # Priority bonus
        if "high-priority" in issue_labels:
            score += 1.0
        elif "medium-priority" in issue_labels:
            score += 0.5
        
        # Good first issue bonus for new interns
        if "good first issue" in issue_labels and intern["current_tasks"] == 0:
            score += 1.0
        
        return score
    
    def assign_tasks(self, max_assignments: int = 10):
        """Assign tasks to interns based on skills and availability"""
        # Get current workload
        workload = self.get_intern_workload()
        
        # Update intern current tasks
        for intern_id, intern in self.interns.items():
            intern["current_tasks"] = workload.get(intern["username"], 0)
        
        # Get unassigned issues
        unassigned_issues = self.get_unassigned_issues()
        
        if not unassigned_issues:
            print("No unassigned issues found.")
            return
        
        print(f"Found {len(unassigned_issues)} unassigned issues")
        
        # Sort issues by priority
        priority_order = ["high-priority", "medium-priority", "low-priority"]
        unassigned_issues.sort(key=lambda issue: 
            min([priority_order.index(label.name) for label in issue.labels 
                 if label.name in priority_order] + [len(priority_order)]))
        
        assignments_made = 0
        
        for issue in unassigned_issues:
            if assignments_made >= max_assignments:
                break
            
            # Find best intern for this task
            best_intern = None
            best_score = -1
            
            for intern_id, intern in self.interns.items():
                # Check if intern can take more tasks
                if intern["current_tasks"] >= intern["max_tasks"]:
                    continue
                
                # Calculate task score
                score = self.calculate_task_score(issue, intern)
                
                if score > best_score:
                    best_score = score
                    best_intern = intern
            
            if best_intern and best_score > 0:
                try:
                    # Assign the issue
                    issue.add_to_assignees(best_intern["username"])
                    
                    # Update workload
                    best_intern["current_tasks"] += 1
                    assignments_made += 1
                    
                    print(f"Assigned '{issue.title}' to {best_intern['name']} (score: {best_score:.1f})")
                    
                except GithubException as e:
                    print(f"Error assigning issue to {best_intern['name']}: {e}")
            else:
                print(f"No suitable intern found for '{issue.title}'")
        
        print(f"\nMade {assignments_made} assignments")
        
        # Print summary
        print("\nCurrent workload:")
        for intern_id, intern in self.interns.items():
            print(f"- {intern['name']}: {intern['current_tasks']}/{intern['max_tasks']} tasks")
    
    def suggest_assignments(self):
        """Suggest assignments without making them"""
        workload = self.get_intern_workload()
        unassigned_issues = self.get_unassigned_issues()
        
        print("Suggested assignments:")
        print("=" * 50)
        
        for issue in unassigned_issues:
            print(f"\nIssue: {issue.title}")
            print(f"Labels: {[label.name for label in issue.labels]}")
            
            suggestions = []
            for intern_id, intern in self.interns.items():
                intern["current_tasks"] = workload.get(intern["username"], 0)
                score = self.calculate_task_score(issue, intern)
                
                if intern["current_tasks"] < intern["max_tasks"]:
                    suggestions.append((intern, score))
            
            suggestions.sort(key=lambda x: x[1], reverse=True)
            
            for intern, score in suggestions[:3]:
                print(f"  - {intern['name']}: {score:.1f} points")


def main():
    parser = argparse.ArgumentParser(description="Assign GitHub issues to interns")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--repo", default="NERD-Community-Ethiopia/generative-ai-course",
                       help="Repository name (owner/repo)")
    parser.add_argument("--max-assignments", type=int, default=10,
                       help="Maximum number of assignments to make")
    parser.add_argument("--suggest-only", action="store_true",
                       help="Only suggest assignments, don't make them")
    
    args = parser.parse_args()
    
    # Create task assigner
    assigner = TaskAssigner(args.token, args.repo)
    
    if args.suggest_only:
        assigner.suggest_assignments()
    else:
        assigner.assign_tasks(args.max_assignments)


if __name__ == "__main__":
    main() 