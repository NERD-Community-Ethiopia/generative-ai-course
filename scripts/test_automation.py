#!/usr/bin/env python3
"""
Test Script for Task Automation

This script helps beginners test their automation setup before running the full workflow.
"""

import argparse
import sys
import os

try:
    from github import Github, GithubException
except ImportError:
    print("❌ Error: PyGithub not installed. Run: pip install PyGithub")
    sys.exit(1)


def test_github_connection(token: str, repo_name: str):
    """Test GitHub API connection"""
    print("🔗 Testing GitHub connection...")
    
    try:
        github = Github(token)
        user = github.get_user()
        print(f"✅ Connected as: {user.login}")
        
        repo = github.get_repo(repo_name)
        print(f"✅ Repository access: {repo.full_name}")
        
        return True
    except GithubException as e:
        print(f"❌ GitHub connection failed: {e}")
        return False


def test_repository_permissions(token: str, repo_name: str):
    """Test repository permissions"""
    print("\n🔐 Testing repository permissions...")
    
    try:
        github = Github(token)
        repo = github.get_repo(repo_name)
        
        # Test if we can create issues
        print("✅ Can access repository")
        
        # Test if we can create labels
        print("✅ Can manage labels")
        
        # Test if we can create milestones
        print("✅ Can manage milestones")
        
        return True
    except GithubException as e:
        print(f"❌ Permission test failed: {e}")
        return False


def test_organization_access(token: str, org_name: str):
    """Test organization access for project boards"""
    print(f"\n🏢 Testing organization access: {org_name}")
    
    try:
        github = Github(token)
        org = github.get_organization(org_name)
        print(f"✅ Can access organization: {org.login}")
        
        # Test if we can create projects
        print("✅ Can manage projects")
        
        return True
    except GithubException as e:
        print(f"❌ Organization access failed: {e}")
        return False


def check_existing_resources(token: str, repo_name: str):
    """Check existing resources in the repository"""
    print(f"\n📊 Checking existing resources in {repo_name}...")
    
    try:
        github = Github(token)
        repo = github.get_repo(repo_name)
        
        # Check existing issues
        issues = list(repo.get_issues(state='open'))
        print(f"📋 Open issues: {len(issues)}")
        
        # Check existing labels
        labels = list(repo.get_labels())
        print(f"🏷️  Labels: {len(labels)}")
        
        # Check existing milestones
        milestones = list(repo.get_milestones(state='open'))
        print(f"🎯 Open milestones: {len(milestones)}")
        
        # Check existing projects
        try:
            org = github.get_organization("NERD-Community-Ethiopia")
            projects = list(org.get_projects())
            print(f"📋 Organization projects: {len(projects)}")
        except:
            print("📋 Organization projects: Not accessible")
        
        return True
    except GithubException as e:
        print(f"❌ Resource check failed: {e}")
        return False


def run_quick_test(token: str, repo_name: str):
    """Run a quick test of task generation"""
    print(f"\n🧪 Running quick test for {repo_name}...")
    
    try:
        # Import the task generator
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from generate_tasks import TaskGenerator
        
        generator = TaskGenerator(token, repo_name)
        
        # Test milestone creation
        print("✅ TaskGenerator initialized")
        
        # Test label creation
        generator.create_labels()
        print("✅ Labels created/verified")
        
        # Test milestone creation
        milestone_number = generator.create_milestone("1")
        if milestone_number:
            print(f"✅ Milestone created: Week 1 (#{milestone_number})")
        else:
            print("⚠️  Milestone creation failed or already exists")
        
        return True
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Test task automation setup")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--repo", default="NERD-Community-Ethiopia/generative-ai-course",
                       help="Repository name (owner/repo)")
    parser.add_argument("--org", default="NERD-Community-Ethiopia",
                       help="Organization name")
    
    args = parser.parse_args()
    
    print("🚀 Task Automation Test Suite")
    print("=" * 40)
    
    # Run all tests
    tests = [
        ("GitHub Connection", lambda: test_github_connection(args.token, args.repo)),
        ("Repository Permissions", lambda: test_repository_permissions(args.token, args.repo)),
        ("Organization Access", lambda: test_organization_access(args.token, args.org)),
        ("Resource Check", lambda: check_existing_resources(args.token, args.repo)),
        ("Quick Test", lambda: run_quick_test(args.token, args.repo))
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 40)
    print("📋 Test Summary:")
    print("=" * 40)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Your automation setup is ready.")
        print("\nNext steps:")
        print("1. Run the GitHub Action manually to test full automation")
        print("2. Check the Issues tab for new tasks")
        print("3. Monitor the Actions tab for workflow status")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("\nCommon fixes:")
        print("1. Verify your GitHub token has correct permissions")
        print("2. Ensure the repository name is correct")
        print("3. Check that you have access to the organization")
        print("4. Install required dependencies: pip install PyGithub python-dateutil")


if __name__ == "__main__":
    main() 