# Generative AI & Automation – Course Repository

Welcome to the official repository for the **Generative AI & Automation** course. This project demonstrates modern software development practices including CI/CD, automated testing, security scanning, and collaborative development workflows.

## 🚀 Quick Links

- **[Student Guide](STUDENT_GUIDE.md)** - How to submit assignments
- **[Intern Guide](INTERN_GUIDE.md)** - Development workflow for team members
- **[Contributing Guidelines](CONTRIBUTING.md)** - Complete contribution guide
- **[Security Policy](security.md)** - Security guidelines and reporting
- **[Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines

## 📚 Course Overview

This is an 8-week intensive course for intermediate/advanced students to gain hands-on experience with:
- Building and deploying generative agents
- Fine-tuning foundation models (LLMs, diffusion)
- Working with multimodal AI (text, image, audio, video)
- Hosting models as APIs and serving them for web and mobile front ends
- Automating model workflows using GitHub Actions, Docker, and APIs
- **Modern Development Practices**: CI/CD, testing, security, collaboration

Each week includes 3 hours of lectures and 3 hours of practical workshops.

## 🏗️ Repository Structure

```
generative-ai-course/
├── .github/                    # GitHub configuration
│   ├── workflows/             # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md
├── lectures/week-01/          # Weekly lecture materials
├── workshops/week-01/         # Workshop starter kits
├── student-submissions/       # Student assignment submissions
├── scripts/                   # Automation and utility scripts
├── tests/                     # Test suite
├── docs/                      # Documentation
├── capstone-projects/         # Final projects
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Modern Python configuration
├── Dockerfile                # Container configuration
├── docker-compose.yml        # Local development setup
├── Makefile                  # Development commands
└── README.md                 # This file
```

## 🔄 CI/CD Pipeline

This project implements a comprehensive CI/CD pipeline that demonstrates real-world development practices:

### Pipeline Stages
1. **Quality Check**: Linting, formatting, type checking
2. **Testing**: Unit and integration tests across Python versions
3. **Security**: Vulnerability scanning with Bandit and Safety
4. **Student Validation**: Automated feedback for submissions
5. **Build**: Docker image creation
6. **Deploy**: Staging and production deployment

### Branch Strategy
- **`main`**: Production-ready code (admin only)
- **`develop`**: Integration branch for contributors
- **`intern/*`**: Personal branches for interns
- **`feature/*`**: Feature development branches
- **`hotfix/*`**: Emergency fixes

### Automated Checks
- ✅ Code formatting (Black)
- ✅ Style checking (Flake8)
- ✅ Type checking (MyPy)
- ✅ Security scanning (Bandit, Safety)
- ✅ Test coverage (Pytest)
- ✅ Student submission validation

## 🚀 Getting Started

### For Students
1. **Fork** this repository to your GitHub account
2. **Clone** your fork locally
3. **Work** in `student-submissions/your-username/week-X/`
4. **Submit** via Pull Request from your fork's main branch

### For Contributors/Interns
1. **Clone** the repository
2. **Create** your personal branch: `intern/your-name`
3. **Install** dependencies: `make install`
4. **Start** development: `make setup`

### For Administrators
1. **Review** PRs to develop branch
2. **Test** develop branch thoroughly
3. **Deploy** to production via main branch
4. **Monitor** CI/CD pipeline health

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- Git
- Docker (optional)
- GitHub account

### Quick Setup
```bash
# Clone repository
git clone https://github.com/NERD-Community-Ethiopia/generative-ai-course.git
cd generative-ai-course

# Install dependencies
make install

# Run quality checks
make quality

# Start development
make setup
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

## 📋 Available Commands

```bash
# Development
make install              # Install dependencies
make test                 # Run tests
make lint                 # Run linting
make format               # Format code
make security             # Security checks
make quality              # All quality checks

# Docker
make docker-build         # Build Docker image
make docker-run           # Run with Docker Compose
make docker-stop          # Stop Docker services

# Utilities
make clean                # Clean temporary files
make docs                 # Build documentation
make validate-submission  # Validate student submission
make dependency-report    # Generate dependency report
make status               # Show project status
```

## 🧪 Testing

### Test Structure
```
tests/
├── unit/              # Unit tests
├── integration/       # Integration tests
├── fixtures/          # Test fixtures
└── conftest.py        # Pytest configuration
```

### Running Tests
```bash
# All tests
make test

# Specific test categories
make test-unit
make test-integration

# With coverage
pytest --cov=./ --cov-report=html
```

## 🔒 Security

### Security Tools
- **Bandit**: Python security linter
- **Safety**: Dependency vulnerability scanner
- **GitHub Security Advisories**: Automated detection

### Security Practices
- Never commit sensitive information
- Use environment variables for configuration
- Follow OWASP Top 10 guidelines
- Keep dependencies updated
- Report vulnerabilities privately

## 📊 Quality Metrics

### Code Quality Standards
- **Test Coverage**: Minimum 80%
- **Code Complexity**: Maximum 10 (McCabe)
- **Security Issues**: Zero critical/high
- **Documentation**: 100% API coverage

### Performance Targets
- **Build Time**: < 10 minutes
- **Test Time**: < 5 minutes
- **Deployment Time**: < 5 minutes

## 🎯 Learning Objectives

By the end of this course, students will be able to:
- Design and implement generative AI agents
- Fine-tune and deploy custom AI models
- Build full-stack applications with AI integration
- Automate AI workflows using modern DevOps practices
- Deploy AI applications to production environments
- **Use professional development tools and practices**
- **Collaborate effectively using Git and GitHub**
- **Write secure, tested, and maintainable code**

## 📅 Course Schedule

- **Week 1**: Introduction to Generative AI & Course Setup
- **Week 2**: Building Your First AI Agent
- **Week 3**: Fine-tuning Foundation Models
- **Week 4**: Multimodal AI Applications
- **Week 5**: API Development & Deployment
- **Week 6**: Frontend Integration & User Experience
- **Week 7**: Automation & CI/CD Pipelines
- **Week 8**: Capstone Project Development

## 🛠️ Tech Stack

### Backend & AI/ML
- **Python**: Core programming language
- **FastAPI/Flask**: Web frameworks
- **PyTorch**: Deep learning framework
- **Transformers**: Hugging Face library
- **LangChain**: AI application framework
- **OpenAI**: API integration

### Development & DevOps
- **Git & GitHub**: Version control and collaboration
- **Docker**: Containerization
- **GitHub Actions**: CI/CD automation
- **Pytest**: Testing framework
- **Black/Flake8**: Code formatting and linting
- **MyPy**: Type checking
- **Bandit/Safety**: Security tools

### Frontend & Deployment
- **React/Vue.js**: Frontend frameworks
- **RESTful APIs**: API design
- **WebSocket**: Real-time communication
- **PostgreSQL/MongoDB**: Databases
- **Vector Databases**: AI data storage

## 🤝 Contributing

### For Students
- Submit assignments via Pull Requests
- Follow the [Student Guide](STUDENT_GUIDE.md)
- Use the student PR template
- Get automated feedback

### For Contributors
- Follow the [Intern Guide](INTERN_GUIDE.md)
- Use feature branches
- Submit PRs to develop branch
- Participate in code reviews

### For Administrators
- Review and merge PRs
- Monitor CI/CD pipeline
- Handle security incidents
- Manage course content

## 📞 Support

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and discussions
- **Element Channels**: Real-time support
- **Office Hours**: Scheduled sessions in discord


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Recognition

### Student Benefits
- **Portfolio Projects**: Each assignment becomes a portfolio piece
- **GitHub Profile**: Professional development history
- **Real-world Skills**: Industry-standard practices
- **Networking**: Connect with other developers

### Contributor Benefits
- **GitHub Contributors**: Recognition in project history
- **Reference Letters**: Professional recommendations
- **Skill Development**: Advanced development practices
- **Career Opportunities**: Industry connections

---

**This course teaches both AI/ML skills and professional software development practices. Students learn to work like real developers while building cutting-edge AI applications.** 