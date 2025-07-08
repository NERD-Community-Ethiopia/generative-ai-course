# GitHub Task Automation Setup Guide

## 🔑 Step 1: Create GitHub Personal Access Token

1. **Go to GitHub Settings**:
   - Log into GitHub
   - Click your profile picture → Settings
   - Scroll down to "Developer settings" (bottom left)
   - Click "Personal access tokens" → "Tokens (classic)"

2. **Generate New Token**:
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name like "Task Automation Token"
   - Set expiration (recommend 90 days for security)

3. **Select Permissions**:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
   - ✅ `admin:org` (Full control of organizations and teams)
   - ✅ `write:packages` (Upload packages to GitHub Package Registry)

4. **Copy the Token**:
   - Click "Generate token"
   - **IMPORTANT**: Copy the token immediately (you won't see it again!)

## 🔒 Step 2: Add Token to Repository Secrets

1. **Go to Repository Settings**:
   - Navigate to your repository: `NERD-Community-Ethiopia/generative-ai-course`
   - Click "Settings" tab

2. **Add Repository Secret**:
   - Click "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `GITHUB_TOKEN`
   - Value: Paste your token from Step 1
   - Click "Add secret"

## 🐍 Step 3: Set Up Python Environment

1. **Install Python Dependencies**:
   ```bash
   pip install PyGithub python-dateutil
   ```

2. **Verify Installation**:
   ```bash
   python -c "import github; print('PyGithub installed successfully!')"
   ```

## 🧪 Step 4: Test the Automation Locally

1. **Test Task Generation**:
   ```bash
   python scripts/generate_tasks.py --week 1 --type all --token YOUR_TOKEN_HERE
   ```

2. **Test Task Assignment**:
   ```bash
   python scripts/assign_tasks.py --token YOUR_TOKEN_HERE
   ```

3. **Test Sprint Board Creation**:
   ```bash
   python scripts/create_sprint_board.py --week 1 --token YOUR_TOKEN_HERE
   ```

## ⚙️ Step 5: Configure the Workflow

### Update Repository Name
If your repository name is different, update these files:
- `scripts/generate_tasks.py` (line 24)
- `scripts/assign_tasks.py` (line 18)
- `scripts/create_sprint_board.py` (line 18)

### Update Intern Information
Edit `scripts/assign_tasks.py` to add real intern usernames:

```python
def _load_interns(self) -> Dict:
    return {
        "intern1": {
            "username": "actual_github_username_1",  # Replace with real username
            "name": "Real Name One",
            "skills": ["python", "ai", "lectures"],
            "preferences": ["lecture", "documentation"],
            "max_tasks": 3,
            "current_tasks": 0
        },
        # Add more interns...
    }
```

## 🚀 Step 6: Run the Automation

### Option A: Manual Trigger (Recommended for Testing)
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click "Agile Task Automation" workflow
4. Click "Run workflow"
5. Fill in the parameters:
   - Week number: `1`
   - Task type: `all`
6. Click "Run workflow"

### Option B: Automatic Schedule
The workflow is set to run every Monday at 9 AM UTC. You can modify the schedule in `.github/workflows/task-automation.yml`:

```yaml
schedule:
  # Run every Monday at 9 AM UTC
  - cron: '0 9 * * 1'
```

## 📊 Step 7: Monitor Results

After running the automation, check:

1. **Issues Tab**: New issues should be created with proper labels and milestones
2. **Projects Tab**: New sprint board should be created (if enabled)
3. **Actions Tab**: Workflow logs show success/failure

## 🔧 Troubleshooting

### Common Issues:

1. **"PyGithub not installed"**:
   ```bash
   pip install PyGithub
   ```

2. **"Authentication failed"**:
   - Check your GitHub token is correct
   - Ensure token has proper permissions
   - Verify token is added to repository secrets

3. **"Repository not found"**:
   - Update repository name in scripts
   - Ensure you have access to the repository

4. **"No template found for week X"**:
   - Check that week number is between 1-8
   - Verify week templates exist in the script

### Debug Mode:
Add `--debug` flag to scripts for more detailed output:
```bash
python scripts/generate_tasks.py --week 1 --type all --token YOUR_TOKEN --debug
```

## 📈 Next Steps

1. **Customize Task Templates**: Edit the task templates in `scripts/generate_tasks.py`
2. **Add More Interns**: Update the intern list in `scripts/assign_tasks.py`
3. **Create Custom Labels**: Add new labels for your specific needs
4. **Set Up Notifications**: Configure GitHub notifications for new issues

## 🎯 Success Indicators

✅ Issues are created with proper labels and milestones
✅ Tasks are assigned to interns automatically
✅ Sprint board is created with proper columns
✅ Workflow runs without errors
✅ Issues appear in the correct milestone

## 📞 Need Help?

If you encounter issues:
1. Check the GitHub Actions logs for error messages
2. Verify all prerequisites are met
3. Test scripts locally first
4. Check GitHub token permissions

---

**Remember**: Keep your GitHub token secure and never commit it to your repository! 