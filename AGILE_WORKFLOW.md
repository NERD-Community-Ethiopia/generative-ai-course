# Agile Workflow & Task Management Guide

This guide explains how to implement and use the automated agile workflow system for the Generative AI & Automation course project.

## 🎯 Overview

Our agile workflow combines GitHub's built-in features with custom automation to provide:
- **Automated task generation** based on course structure
- **Smart task assignment** based on intern skills and availability
- **Sprint management** with GitHub Projects boards
- **Progress tracking** and reporting
- **Automated notifications** and reminders

## 🚀 Quick Start

### 1. Initial Setup

```bash
# Install required dependencies
pip install PyGithub python-dateutil

# Set up GitHub token with appropriate permissions
# Go to GitHub Settings → Developer settings → Personal access tokens
# Create token with: repo, admin:org, project permissions
```

### 2. Generate Your First Tasks

```bash
# Generate tasks for Week 1
python scripts/generate_tasks.py --week 1 --token YOUR_GITHUB_TOKEN

# Generate specific task types
python scripts/generate_tasks.py --week 2 --type lecture --token YOUR_GITHUB_TOKEN
```

### 3. Assign Tasks to Interns

```bash
# Auto-assign tasks based on skills and availability
python scripts/assign_tasks.py --token YOUR_GITHUB_TOKEN

# Preview assignments without making them
python scripts/assign_tasks.py --token YOUR_GITHUB_TOKEN --suggest-only
```

### 4. Create Sprint Board

```bash
# Create weekly sprint board
python scripts/create_sprint_board.py --week 1 --token YOUR_GITHUB_TOKEN

# List existing boards
python scripts/create_sprint_board.py --list-boards --token YOUR_GITHUB_TOKEN
```

## 📋 Workflow Components

### 1. Task Generation (`generate_tasks.py`)

**What it does:**
- Creates GitHub issues for each week's tasks
- Organizes tasks by type (lecture, workshop, assignment, documentation)
- Sets appropriate labels and priorities
- Creates milestones for each week

**Task Types:**
- **Lecture**: Course content creation
- **Workshop**: Hands-on exercises
- **Assignment**: Student assignments
- **Documentation**: Guides and documentation

**Priority Levels:**
- **High Priority**: Critical path items
- **Medium Priority**: Important but not blocking
- **Low Priority**: Nice-to-have improvements

### 2. Task Assignment (`assign_tasks.py`)

**Assignment Logic:**
- **Skill Matching**: Assigns tasks based on intern skills
- **Preference Matching**: Considers intern preferences
- **Workload Balancing**: Ensures fair distribution
- **Priority Consideration**: High-priority tasks get preference

**Intern Profiles:**
```python
{
    "username": "intern1",
    "name": "Intern One",
    "skills": ["python", "ai", "lectures"],
    "preferences": ["lecture", "documentation"],
    "max_tasks": 3,
    "current_tasks": 0
}
```

### 3. Sprint Management (`create_sprint_board.py`)

**Board Structure:**
- **Backlog**: Unassigned tasks
- **To Do**: Assigned but not started
- **In Progress**: Currently being worked on
- **Review**: Ready for review
- **Done**: Completed tasks

## 🔄 Weekly Workflow

### Monday: Sprint Planning

1. **Generate Weekly Tasks**
   ```bash
   python scripts/generate_tasks.py --week 1 --token YOUR_TOKEN
   ```

2. **Create Sprint Board**
   ```bash
   python scripts/create_sprint_board.py --week 1 --token YOUR_TOKEN
   ```

3. **Assign Tasks**
   ```bash
   python scripts/assign_tasks.py --token YOUR_TOKEN
   ```

### Daily: Task Management

1. **Interns move their tasks** through the board columns
2. **Create PRs** when tasks are ready for review
3. **Update task status** based on progress

### Friday: Sprint Review

1. **Review completed tasks**
2. **Update sprint metrics**
3. **Plan next week's tasks**

## 🎯 Task Categories & Templates

### Lecture Tasks
- **Template**: Create comprehensive lecture materials
- **Deliverables**: README.md, slides, code examples
- **Timeline**: 2-3 days
- **Skills**: Content creation, AI knowledge

### Workshop Tasks
- **Template**: Design hands-on exercises
- **Deliverables**: Exercise files, solutions, instructions
- **Timeline**: 2-3 days
- **Skills**: Python, teaching, problem-solving

### Assignment Tasks
- **Template**: Create student assignments
- **Deliverables**: Assignment description, rubric, test cases
- **Timeline**: 1-2 days
- **Skills**: Assessment design, clear communication

### Documentation Tasks
- **Template**: Update and improve documentation
- **Deliverables**: Updated guides, troubleshooting docs
- **Timeline**: 1 day
- **Skills**: Technical writing, organization

## 🤖 Automation Features

### GitHub Actions Integration

The workflow automatically:
- **Runs every Monday** at 9 AM UTC
- **Generates tasks** for the current week
- **Creates sprint boards** for organization
- **Sends notifications** to team members

### Manual Triggers

You can also trigger automation manually:
- **Generate specific tasks**: Use workflow dispatch
- **Reassign tasks**: Run assignment script
- **Create custom sprints**: Use board creation script

### Notifications

- **Task assignments**: Interns get notified when assigned
- **Sprint updates**: Team gets weekly progress reports
- **Deadline reminders**: Automated reminders for due dates

## 📊 Metrics & Reporting

### Sprint Metrics
- **Velocity**: Tasks completed per sprint
- **Burndown**: Progress over time
- **Capacity**: Intern workload distribution
- **Quality**: Code review metrics

### Individual Metrics
- **Tasks completed**: Per intern
- **Average completion time**: Per task type
- **Code quality**: Based on CI/CD results
- **Collaboration**: PR reviews and comments

## 🛠️ Configuration

### Customizing Task Templates

Edit `scripts/generate_tasks.py` to modify:
- Task descriptions and requirements
- Priority assignments
- Skill requirements
- Timeline estimates

### Customizing Intern Profiles

Edit `scripts/assign_tasks.py` to update:
- Intern skills and preferences
- Maximum task limits
- Assignment weights
- Team structure

### Customizing Sprint Boards

Edit `scripts/create_sprint_board.py` to modify:
- Board column structure
- Automation rules
- Issue filtering
- Board templates

## 🔧 Advanced Features

### 1. Dependency Management

Tasks can have dependencies:
```python
{
    "title": "Create Week 2 Workshop",
    "dependencies": ["Create Week 2 Lecture"],
    "blocked_by": ["week-2-lecture"]
}
```

### 2. Skill-Based Routing

Advanced assignment logic:
- **Primary skills**: Direct task matches
- **Secondary skills**: Backup assignments
- **Learning opportunities**: Skill development tasks
- **Mentorship**: Pair programming assignments

### 3. Automated Reviews

- **Code review assignment**: Based on expertise
- **Documentation review**: Technical writers
- **Content review**: Subject matter experts
- **Final review**: Administrators

## 📈 Best Practices

### For Administrators

1. **Plan Ahead**: Generate tasks 1-2 weeks in advance
2. **Balance Workload**: Monitor intern capacity
3. **Provide Feedback**: Regular check-ins and reviews
4. **Adapt Process**: Adjust based on team feedback

### For Interns

1. **Update Status**: Move tasks through board columns
2. **Communicate**: Comment on issues with progress
3. **Ask Questions**: Use issue comments for clarification
4. **Collaborate**: Help review others' work

### For the Team

1. **Daily Standups**: Quick status updates
2. **Weekly Reviews**: Sprint planning and retrospectives
3. **Continuous Improvement**: Regular process adjustments
4. **Documentation**: Keep process documentation updated

## 🚨 Troubleshooting

### Common Issues

**Tasks not generating:**
- Check GitHub token permissions
- Verify repository access
- Check script dependencies

**Assignments not working:**
- Verify intern usernames
- Check workload limits
- Review skill configurations

**Board creation fails:**
- Check organization permissions
- Verify project creation rights
- Review board templates

### Debug Commands

```bash
# Test task generation
python scripts/generate_tasks.py --week 1 --type lecture --token YOUR_TOKEN

# Preview assignments
python scripts/assign_tasks.py --token YOUR_TOKEN --suggest-only

# List existing boards
python scripts/create_sprint_board.py --list-boards --token YOUR_TOKEN
```

## 📚 Resources

### Documentation
- [GitHub Issues API](https://docs.github.com/en/rest/issues)
- [GitHub Projects API](https://docs.github.com/en/rest/projects)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)

### Templates
- [Issue Templates](.github/ISSUE_TEMPLATE/)
- [PR Templates](.github/pull_request_template.md)
- [Workflow Templates](.github/workflows/)

### Tools
- [GitHub CLI](https://cli.github.com/)
- [GitHub Desktop](https://desktop.github.com/)
- [GitHub Projects](https://github.com/features/project-management/)

## 🎉 Success Metrics

### Short-term Goals
- [ ] All tasks automatically generated
- [ ] Tasks assigned within 24 hours
- [ ] Sprint boards created weekly
- [ ] 80% task completion rate

### Long-term Goals
- [ ] Zero manual task management
- [ ] 95% task completion rate
- [ ] Reduced sprint planning time by 50%
- [ ] Improved intern satisfaction scores

---

*This agile workflow system is designed to scale with your team and adapt to changing needs. Regular feedback and iteration will ensure it continues to serve your project effectively.* 