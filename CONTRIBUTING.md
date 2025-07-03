# Contributing to Generative AI & Automation Course

Thank you for your interest in contributing to this course! This document provides comprehensive guidelines for students, contributors, and administrators.

## 🚀 Quick Links

- **[Intern Guide](INTERN_GUIDE.md)** - For interns working on course development
- **[Student Guide](STUDENT_GUIDE.md)** - For students submitting assignments
- **[Security Policy](security.md)** - Security guidelines and reporting
- **[Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines

## 🏗️ Project Structure

```
generative-ai-course/
├── .github/                    # GitHub configuration
│   ├── workflows/             # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md
├── lectures/                  # Course lecture materials
├── workshops/                 # Hands-on workshop materials
├── student-submissions/       # Student assignment submissions
├── scripts/                   # Automation and utility scripts
├── tests/                     # Test suite
├── docs/                      # Documentation
└── capstone-projects/         # Final projects
```

## 🎓 For Students

**Please see [STUDENT_GUIDE.md](STUDENT_GUIDE.md) for detailed submission instructions.**

### Quick Overview

- Fork the repository
- Work in `student-submissions/your-username/week-X/`
- Submit PRs from your fork's main branch
- No feature branches needed

### Learning Objectives

This course teaches you:

- Modern software development practices
- CI/CD workflows and automation
- Code quality and security best practices
- Collaborative development with Git
- Professional project management

## 👥 For Contributors (Interns & Team Members)

**Please see [INTERN_GUIDE.md](INTERN_GUIDE.md) for detailed workflow instructions.**

### Quick Overview

- Get your personal branch: `intern/your-name` or `contributor/your-name`
- Work on course materials and development
- Submit PRs from your branch to `develop`
- Coordinate with other contributors

### Development Workflow

1. **Setup**: Clone repo and create your branch
2. **Development**: Work on assigned features
3. **Testing**: Run tests and quality checks
4. **Review**: Submit PR for review
5. **Merge**: Merge to develop after approval

## 👨‍💼 For Administrators

### Responsibilities

- Review and merge PRs to main branch
- Manage course content and structure
- Monitor CI/CD pipeline health
- Handle security incidents
- Coordinate with contributors

### Deployment Process

1. **Review develop branch**: Ensure all tests pass
2. **Create release PR**: develop → main
3. **Final review**: Security and functionality check
4. **Deploy**: Automated deployment to production
5. **Monitor**: Ensure successful deployment

## 🔧 Development Setup

### Prerequisites

- Python 3.8+
- Git
- Docker (optional)
- GitHub account

### Local Setup

```bash
# Clone the repository
git clone https://github.com/NERD-Community-Ethiopia/generative-ai-course.git
cd generative-ai-course

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

### Docker Setup (Alternative)

```bash
# Build and run with Docker Compose
docker-compose up -d

# Run specific services
docker-compose up jupyter  # Jupyter Lab
docker-compose up tests    # Run tests
docker-compose up lint     # Run linting
```

## 📋 Code Quality Standards

### Python Style Guide

- **Formatter**: Black (line length: 88)
- **Linter**: Flake8
- **Type Checker**: MyPy
- **Security**: Bandit
- **Dependencies**: Safety

### Code Review Checklist

- [ ] Code follows style guidelines
- [ ] Tests are included and pass
- [ ] Documentation is updated
- [ ] No security vulnerabilities
- [ ] No breaking changes
- [ ] Performance considerations

### Commit Message Convention

```
type(scope): description

[optional body]

[optional footer]
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Maintenance tasks

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=./ --cov-report=html

# Run specific test categories
pytest -m unit
pytest -m integration
pytest -m slow

# Run tests in parallel
pytest -n auto
```

### Test Structure

```
tests/
├── unit/              # Unit tests
├── integration/       # Integration tests
├── fixtures/          # Test fixtures
└── conftest.py        # Pytest configuration
```

## 🔒 Security

### Security Guidelines

- Never commit sensitive information
- Use environment variables for configuration
- Follow OWASP Top 10 guidelines
- Keep dependencies updated
- Report vulnerabilities privately

### Security Tools

- **Bandit**: Python security linter
- **Safety**: Dependency vulnerability scanner
- **GitHub Security Advisories**: Automated detection

## 📚 Documentation

### Documentation Standards

- Use clear, concise language
- Include code examples
- Keep documentation up to date
- Use proper formatting (Markdown)

### Documentation Structure

```
docs/
├── getting-started.md
├── api-reference.md
├── tutorials/
├── examples/
└── troubleshooting.md
```

## 🤝 Collaboration

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and discussions
- **Pull Requests**: Code reviews and feedback
- **Wiki**: Course documentation and guides

### Code Review Process

1. **Submit PR**: Create pull request with description
2. **Automated Checks**: CI/CD pipeline runs tests
3. **Review**: Team members review code
4. **Feedback**: Address review comments
5. **Approval**: Get required approvals
6. **Merge**: Merge after all checks pass

### Conflict Resolution

- Be respectful and constructive
- Focus on the code, not the person
- Provide specific, actionable feedback
- Use evidence and examples
- Escalate to administrators if needed

## 🚀 CI/CD Pipeline

### Pipeline Stages

1. **Quality Check**: Linting, formatting, type checking
2. **Testing**: Unit and integration tests
3. **Security**: Vulnerability scanning
4. **Build**: Docker image creation
5. **Deploy**: Staging and production deployment

### Pipeline Triggers

- **Push to main/develop**: Full pipeline
- **Pull Request**: Quality checks and testing
- **Student Submission**: Validation and feedback
- **Scheduled**: Security and dependency checks

## 📊 Quality Metrics

### Code Quality

- **Test Coverage**: Minimum 80%
- **Code Complexity**: Maximum 10 (McCabe)
- **Security Issues**: Zero critical/high
- **Documentation**: 100% API coverage

### Performance

- **Build Time**: < 10 minutes
- **Test Time**: < 5 minutes
- **Deployment Time**: < 5 minutes

## 🎯 Contribution Areas

### High Priority

- Course content development
- Bug fixes and improvements
- Security enhancements
- Documentation updates

### Medium Priority

- Feature additions
- Performance optimizations
- Tool integrations
- Testing improvements

### Low Priority

- Nice-to-have features
- Cosmetic improvements
- Experimental features

## 🏆 Recognition

### Contributor Recognition

- GitHub contributors list
- Course acknowledgments
- Reference letters (upon request)
- Portfolio projects

### Student Recognition

- Course completion certificates
- GitHub profile showcases
- Portfolio additions
- Networking opportunities

## 📞 Getting Help

### Support Resources

- **Documentation**: Check docs first
- **GitHub Issues**: For technical problems
- **Discussions**: For questions and ideas
- **Office Hours**: Scheduled sessions

### Emergency Contacts

- **Security Issues**: security@example.com
- **Technical Problems**: tech-support@example.com
- **Course Questions**: course-instructor@example.com

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to the Generative AI & Automation course!** Your participation helps make this course better for everyone and teaches valuable real-world development skills.
