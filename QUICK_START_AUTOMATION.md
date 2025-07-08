# 🚀 Quick Start: Task Automation Setup

## ⚡ 5-Minute Setup Guide

### Step 1: Get GitHub Token (2 minutes)
1. Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Name: `Task Automation`
4. Select permissions: `repo`, `workflow`, `admin:org`
5. Copy the token (starts with `ghp_`)

### Step 2: Add Token to Repository (1 minute)
1. Go to your repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GITHUB_TOKEN`
4. Value: Paste your token
5. Click "Add secret"

### Step 3: Test Setup (2 minutes)
```bash
# Install dependencies
pip install PyGithub python-dateutil

# Test your setup
python scripts/test_automation.py --token YOUR_TOKEN_HERE
```

### Step 4: Run Automation
1. Go to repository → Actions tab
2. Click "Agile Task Automation"
3. Click "Run workflow"
4. Fill in: Week `1`, Type `all`
5. Click "Run workflow"

## 🎯 What This Does

✅ **Creates Issues**: Generates GitHub issues for weekly tasks
✅ **Assigns Tasks**: Automatically assigns tasks to interns
✅ **Creates Milestones**: Organizes tasks by week
✅ **Sets Up Labels**: Categorizes tasks (lecture, workshop, etc.)
✅ **Creates Sprint Boards**: Manages workflow with Kanban boards

## 📋 Expected Results

After running, you should see:
- 4 new issues in the Issues tab
- 1 new milestone "Week 1"
- New labels (lecture, workshop, assignment, documentation)
- Tasks assigned to interns (if configured)

## 🔧 Troubleshooting

**"PyGithub not installed"**
```bash
pip install PyGithub
```

**"Authentication failed"**
- Check token permissions
- Verify token is in repository secrets

**"Repository not found"**
- Update repository name in scripts
- Ensure you have repository access

## 📞 Need Help?

1. Run the test script first: `python scripts/test_automation.py --token YOUR_TOKEN`
2. Check the detailed guide: `GITHUB_SETUP_GUIDE.md`
3. Look at workflow logs in Actions tab

---

**🎉 You're ready to automate your course management!** 