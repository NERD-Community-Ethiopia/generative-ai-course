# 🚀 NERD Dev Onboarding Sprint — Week 1: Complete Guide

## 📋 Overview

This guide will walk you through completing all 50 tasks in the NERDD Dev Onboarding Sprint Week 1. The tasks are organized into four main categories:
- **Cursor Setup** (11 tasks)
- **Git Fundamentals** (18 tasks)
- **Docker Basics** (16 tasks)
- **Workflow Integration** (5 tasks)

## 🎯 Prerequisites

Before starting, ensure you have:
- A computer with internet access
- Administrator privileges for software installation
- A GitHub account
- Basic familiarity with command line/terminal

---

## 🖥️ Section 1: Cursor Setup (11 Tasks)

### Task 1: Install Cursor and sign in with GitHub

1. **Download Cursor**:
   - Go to [cursor.sh](https://cursor.sh)
   - Click "Download for [Your OS]"
   - Run the installer and follow the setup wizard

2. **Sign in with GitHub**:
   - Open Cursor
   - Click "Sign in with GitHub"
   - Authorize Cursor to access your GitHub account
   - Complete the authentication process

### Task 2: Open a project folder in Cursor

1. **Create a project folder**:
   ```bash
   mkdir NERD-dev-onboarding
   cd NERD-dev-onboarding
   ```

2. **Open in Cursor**:
   - In Cursor, go to `File → Open Folder`
   - Navigate to your `NERD-dev-onboarding` folder
   - Click "Select Folder"

### Task 3: Use built-in terminal in Cursor

1. **Open terminal**:
   - Press `Ctrl + `` (backtick) or `Cmd + `` on Mac
   - Or go to `Terminal → New Terminal`
   - The terminal will open at the bottom of the window

2. **Test the terminal**:
   ```bash
   pwd
   ls
   echo "Terminal is working!"
   ```

### Task 4: Install one Cursor extension

1. **Open Extensions**:
   - Press `Ctrl + Shift + X` or `Cmd + Shift + X` on Mac
   - Or click the Extensions icon in the sidebar

2. **Install a useful extension**:
   - Search for "Python" or "JavaScript" or "GitLens"
   - Click "Install" on your chosen extension
   - Restart Cursor if prompted

### Task 5: Create index.html and style.css

1. **Create index.html**:
   ```bash
   touch index.html
   ```

2. **Add basic HTML structure**:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>NERD Dev Onboarding</title>
       <link rel="stylesheet" href="style.css">
   </head>
   <body>
       <h1>Welcome to NERD Dev Onboarding!</h1>
       <p>This is my first project with Cursor.</p>
       <script src="script.js"></script>
   </body>
   </html>
   ```

3. **Create style.css**:
   ```bash
   touch style.css
   ```

4. **Add basic CSS**:
   ```css
   body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 20px;
       background-color: #f0f0f0;
   }
   
   h1 {
       color: #333;
       text-align: center;
   }
   
   p {
       color: #666;
       text-align: center;
   }
   ```

### Task 6: Write a JS console.log() program

1. **Create script.js**:
   ```bash
   touch script.js
   ```

2. **Add JavaScript code**:
   ```javascript
   console.log("Hello from NERD Dev Onboarding!");
   console.log("Current date:", new Date().toLocaleDateString());
   console.log("User agent:", navigator.userAgent);
   
   // Simple function
   function greetUser(name) {
       console.log(`Welcome, ${name}!`);
   }
   
   greetUser("Developer");
   ```

### Task 7: Use AI autocomplete in Cursor

1. **Enable AI autocomplete**:
   - Press `Ctrl + Shift + P` to open command palette
   - Type "Cursor: Toggle AI Autocomplete"
   - Press Enter to enable

2. **Test autocomplete**:
   - Open `script.js`
   - Start typing: `const user = {`
   - Let Cursor suggest the completion
   - Press `Tab` to accept suggestions

### Task 8: Ask Cursor to explain code

1. **Select code to explain**:
   - Highlight the JavaScript code in `script.js`
   - Press `Ctrl + K` or `Cmd + K` on Mac
   - Type: "Explain this code"
   - Press Enter

2. **Alternative method**:
   - Right-click on selected code
   - Choose "Ask Cursor" from context menu
   - Ask your question

### Task 9: Format code with keyboard shortcut

1. **Format HTML**:
   - Open `index.html`
   - Press `Shift + Alt + F` (Windows) or `Shift + Option + F` (Mac)
   - The code will be automatically formatted

2. **Format CSS**:
   - Open `style.css`
   - Press the same shortcut
   - CSS will be formatted

3. **Format JavaScript**:
   - Open `script.js`
   - Use the same formatting shortcut

### Task 10: Create a README.md in markdown

1. **Create README.md**:
   ```bash
   touch README.md
   ```

2. **Add markdown content**:
   ```markdown
   # NERD Dev Onboarding Project

   ## Description
   This project demonstrates the skills learned during the NERD Dev Onboarding Sprint Week 1.

   ## Files
   - `index.html` - Main HTML file
   - `style.css` - CSS styling
   - `script.js` - JavaScript functionality
   - `README.md` - This file

   ## Setup
   1. Clone this repository
   2. Open `index.html` in a web browser
   3. Open browser console to see JavaScript output

   ## Features
   - Basic HTML structure
   - CSS styling
   - JavaScript console logging
   - Responsive design

   ## Learning Outcomes
   - Cursor IDE setup and usage
   - Basic web development
   - AI-assisted coding
   - Code formatting and documentation
   ```

### Task 11: Test your setup

1. **Open index.html in browser**:
   - Right-click `index.html` in Cursor
   - Select "Open with Live Server" or open in your default browser
   - Open browser console (F12) to see JavaScript output

---

## 🔄 Section 2: Git Fundamentals (18 Tasks)

### Task 12: Install Git and set up user config

1. **Install Git**:
   - **Windows**: Download from [git-scm.com](https://git-scm.com/)
   - **Mac**: `brew install git` (if you have Homebrew) or download installer
   - **Linux**: `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/RHEL)

2. **Configure Git**:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Verify installation**:
   ```bash
   git --version
   git config --list
   ```

### Task 13: Run git init in a project

1. **Initialize Git repository**:
   ```bash
   cd NERD-dev-onboarding
   git init
   ```

2. **Verify initialization**:
   ```bash
   ls -la
   # You should see a .git folder
   ```

### Task 14: Add files with git add .

1. **Add all files**:
   ```bash
   git add .
   ```

2. **Check status**:
   ```bash
   git status
   # Should show all files as "staged for commit"
   ```

### Task 15: Commit with git commit -m

1. **Make your first commit**:
   ```bash
   git commit -m "Initial commit: Add HTML, CSS, JS, and README files"
   ```

2. **Verify commit**:
   ```bash
   git log --oneline
   ```

### Task 16: Check git status

1. **Check current status**:
   ```bash
   git status
   # Should show "working tree clean"
   ```

2. **Make a change and check status**:
   ```bash
   echo "# Updated README" >> README.md
   git status
   # Should show README.md as modified
   ```

### Task 17: View history with git log

1. **View commit history**:
   ```bash
   git log
   ```

2. **View compact history**:
   ```bash
   git log --oneline
   ```

3. **View history with graph**:
   ```bash
   git log --graph --oneline --all
   ```

### Task 18: Create .gitignore

1. **Create .gitignore file**:
   ```bash
   touch .gitignore
   ```

2. **Add common ignore patterns**:
   ```bash
   # Dependencies
   node_modules/
   npm-debug.log*
   yarn-debug.log*
   yarn-error.log*
   
   # Environment variables
   .env
   .env.local
   .env.development.local
   .env.test.local
   .env.production.local
   
   # IDE files
   .vscode/
   .idea/
   *.swp
   *.swo
   
   # OS files
   .DS_Store
   Thumbs.db
   
   # Logs
   logs
   *.log
   
   # Runtime data
   pids
   *.pid
   *.seed
   *.pid.lock
   
   # Coverage directory used by tools like istanbul
   coverage/
   
   # Temporary folders
   tmp/
   temp/
   ```

### Task 19: Create new branch feature/test

1. **Create and switch to new branch**:
   ```bash
   git checkout -b feature/test
   ```

2. **Verify branch creation**:
   ```bash
   git branch
   # Should show feature/test with an asterisk
   ```

### Task 20: Switch to another branch

1. **Switch back to main branch**:
   ```bash
   git checkout main
   ```

2. **Switch back to feature branch**:
   ```bash
   git checkout feature/test
   ```

### Task 21: Merge branches

1. **Make changes in feature branch**:
   ```bash
   echo "This is a test feature" > test-feature.txt
   git add test-feature.txt
   git commit -m "Add test feature file"
   ```

2. **Switch to main and merge**:
   ```bash
   git checkout main
   git merge feature/test
   ```

3. **Verify merge**:
   ```bash
   ls
   # Should show test-feature.txt
   git log --oneline
   ```

### Task 22: Resolve a merge conflict

1. **Create conflict scenario**:
   ```bash
   # In main branch
   echo "Main branch content" > conflict-file.txt
   git add conflict-file.txt
   git commit -m "Add conflict file in main"
   
   # In feature branch
   git checkout feature/test
   echo "Feature branch content" > conflict-file.txt
   git add conflict-file.txt
   git commit -m "Add conflict file in feature"
   ```

2. **Attempt merge to create conflict**:
   ```bash
   git checkout main
   git merge feature/test
   # This will show a merge conflict
   ```

3. **Resolve conflict**:
   - Open `conflict-file.txt` in Cursor
   - You'll see conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
   - Edit the file to resolve the conflict:
   ```txt
   Main branch content
   Feature branch content
   Combined content
   ```

4. **Complete merge**:
   ```bash
   git add conflict-file.txt
   git commit -m "Resolve merge conflict"
   ```

### Task 23: Connect to GitHub (HTTPS/SSH)

1. **Create GitHub repository**:
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name it "NERD-dev-onboarding"
   - Don't initialize with README (we already have one)
   - Click "Create repository"

2. **Connect using HTTPS**:
   ```bash
   git remote add origin https://github.com/your-username/NERD-dev-onboarding.git
   ```

3. **Alternative: Connect using SSH** (if you have SSH keys set up -- refer to the -SSh configuration guid):
   ```bash
   git remote add origin git@github.com:your-username/NERD-dev-onboarding.git
   ```

4. **Verify remote**:
   ```bash
   git remote -v
   ```

### Task 24: Push local repo to GitHub

1. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```

2. **Verify push**:
   - Go to your GitHub repository
   - You should see all your files there

### Task 25: Pull remote changes

1. **Simulate remote changes**:
   - Go to your GitHub repository
   - Edit README.md online
   - Add a line like "Updated from GitHub web interface"
   - Commit the change

2. **Pull changes locally**:
   ```bash
   git pull origin main
   ```

3. **Verify changes**:
   ```bash
   cat README.md
   # Should show the new line
   ```

### Task 26: Create a new branch and push it

1. **Create and switch to new branch**:
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make changes**:
   ```bash
   echo "New feature content" > new-feature.txt
   git add new-feature.txt
   git commit -m "Add new feature"
   ```

3. **Push new branch**:
   ```bash
   git push -u origin feature/new-feature
   ```

### Task 27: Clone repository on another location

1. **Clone to a different directory**:
   ```bash
   cd ..
   git clone https://github.com/your-username/NERD-dev-onboarding.git NERD-dev-onboarding-clone
   cd NERD-dev-onboarding-clone
   ```

2. **Verify clone**:
   ```bash
   ls
   git log --oneline
   ```

### Task 28: Fetch and merge changes

1. **Fetch remote changes**:
   ```bash
   git fetch origin
   ```

2. **Check what's available**:
   ```bash
   git branch -r
   ```

3. **Merge specific branch**:
   ```bash
   git merge origin/feature/new-feature
   ```

### Task 29: Stash changes

1. **Make uncommitted changes**:
   ```bash
   echo "Uncommitted work" > work-in-progress.txt
   ```

2. **Stash changes**:
   ```bash
   git stash
   ```

3. **Check stash**:
   ```bash
   git stash list
   ```

4. **Apply stash**:
   ```bash
   git stash pop
   ```

---

## 🐳 Section 3: Docker Basics (16 Tasks)

### Task 30: Install Docker

1. **Install Docker Desktop**:
   - **Windows/Mac**: Download from [docker.com](https://www.docker.com/products/docker-desktop/)
   - **Linux**: Follow distribution-specific instructions at [docs.docker.com](https://docs.docker.com/engine/install/)

2. **Start Docker**:
   - Launch Docker Desktop
   - Wait for Docker to start (green icon in system tray)

### Task 31: Check Docker version

1. **Verify installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

2. **Test Docker**:
   ```bash
   docker run hello-world
   ```

### Task 32: Create a Dockerfile for Node app

1. **Create a simple Node.js app**:
   ```bash
   mkdir docker-node-app
   cd docker-node-app
   ```

2. **Create package.json**:
   ```json
   {
     "name": "docker-node-app",
     "version": "1.0.0",
     "description": "Simple Node.js app for Docker testing",
     "main": "app.js",
     "scripts": {
       "start": "node app.js"
     },
     "dependencies": {
       "express": "^4.18.2"
     }
   }
   ```

3. **Create app.js**:
   ```javascript
   const express = require('express');
   const app = express();
   const port = process.env.PORT || 3000;
   
   app.get('/', (req, res) => {
     res.json({
       message: 'Hello from Docker!',
       timestamp: new Date().toISOString(),
       environment: process.env.NODE_ENV || 'development'
     });
   });
   
   app.listen(port, () => {
     console.log(`Server running on port ${port}`);
   });
   ```

4. **Create Dockerfile**:
   ```dockerfile
   # Use official Node.js runtime as base image
   FROM node:18-alpine
   
   # Set working directory
   WORKDIR /app
   
   # Copy package files
   COPY package*.json ./
   
   # Install dependencies
   RUN npm install
   
   # Copy application code
   COPY . .
   
   # Expose port
   EXPOSE 3000
   
   # Start the application
   CMD ["npm", "start"]
   ```

### Task 33: Build Docker image

1. **Build the image**:
   ```bash
   docker build -t my-node-app .
   ```

2. **Verify build**:
   ```bash
   docker images
   # Should show my-node-app in the list
   ```

### Task 34: Run Docker contaiNERD

1. **Run the contaiNERD**:
   ```bash
   docker run -p 3000:3000 my-node-app
   ```

2. **Test the application**:
   - Open browser to `http://localhost:3000`
   - Or use curl: `curl http://localhost:3000`

### Task 35: View running contaiNERDs docker ps

1. **Check running contaiNERDs**:
   ```bash
   docker ps
   ```

2. **Check all contaiNERDs (including stopped)**:
   ```bash
   docker ps -a
   ```

### Task 36: Stop/remove contaiNERD

1. **Stop the contaiNERD**:
   ```bash
   # Get contaiNERD ID from docker ps
   docker stop <contaiNERD-id>
   ```

2. **Remove the contaiNERD**:
   ```bash
   docker rm <contaiNERD-id>
   ```

3. **Stop and remove in one command**:
   ```bash
   docker rm -f <contaiNERD-id>
   ```

### Task 37: Create .dockerignore

1. **Create .dockerignore file**:
   ```bash
   touch .dockerignore
   ```

2. **Add ignore patterns**:
   ```
   node_modules
   npm-debug.log
   .git
   .gitignore
   README.md
   .env
   .dockerignore
   Dockerfile
   docker-compose.yml
   ```

### Task 38: Add .env and use in contaiNERD

1. **Create .env file**:
   ```bash
   touch .env
   ```

2. **Add environment variables**:
   ```
   NODE_ENV=development
   PORT=3000
   MESSAGE=Hello from environment variable!
   ```

3. **Update app.js to use environment variables**:
   ```javascript
   const express = require('express');
   const app = express();
   const port = process.env.PORT || 3000;
   
   app.get('/', (req, res) => {
     res.json({
       message: process.env.MESSAGE || 'Hello from Docker!',
       timestamp: new Date().toISOString(),
       environment: process.env.NODE_ENV || 'development'
     });
   });
   
   app.listen(port, () => {
     console.log(`Server running on port ${port}`);
   });
   ```

4. **Run with environment file**:
   ```bash
   docker run -p 3000:3000 --env-file .env my-node-app
   ```

### Task 39: Expose port 3000

1. **The Dockerfile already exposes port 3000**, but let's verify:
   ```dockerfile
   EXPOSE 3000
   ```

2. **Run with port mapping**:
   ```bash
   docker run -p 3000:3000 my-node-app
   ```

3. **Test different port mapping**:
   ```bash
   docker run -p 8080:3000 my-node-app
   # Now access at http://localhost:8080
   ```

### Task 40: Use docker-compose

1. **Create docker-compose.yml**:
   ```yaml
   version: '3.8'
   
   services:
     app:
       build: .
       ports:
         - "3000:3000"
       environment:
         - NODE_ENV=development
         - PORT=3000
       env_file:
         - .env
       volumes:
         - .:/app
         - /app/node_modules
       restart: unless-stopped
   ```

2. **Run with docker-compose**:
   ```bash
   docker-compose up
   ```

3. **Run in background**:
   ```bash
   docker-compose up -d
   ```

4. **Stop services**:
   ```bash
   docker-compose down
   ```

### Task 41: Pull Docker image from DockerHub

1. **Pull a public image**:
   ```bash
   docker pull nginx:alpine
   ```

2. **Verify the pull**:
   ```bash
   docker images
   # Should show nginx:alpine
   ```

### Task 42: Tag & push image to DockerHub

1. **Create DockerHub account** (if you don't have one):
   - Go to [hub.docker.com](https://hub.docker.com)
   - Sign up for a free account

2. **Login to DockerHub**:
   ```bash
   docker login
   ```

3. **Tag your image**:
   ```bash
   docker tag my-node-app your-username/my-node-app:latest
   ```

4. **Push to DockerHub**:
   ```bash
   docker push your-username/my-node-app:latest
   ```

### Task 43: View logs with docker logs

1. **Run contaiNERD in background**:
   ```bash
   docker run -d -p 3000:3000 my-node-app
   ```

2. **View logs**:
   ```bash
   # Get contaiNERD ID
   docker ps
   
   # View logs
   docker logs <contaiNERD-id>
   
   # Follow logs in real-time
   docker logs -f <contaiNERD-id>
   ```

### Task 44: Remove image with docker rmi

1. **List images**:
   ```bash
   docker images
   ```

2. **Remove specific image**:
   ```bash
   docker rmi my-node-app
   ```

3. **Remove all unused images**:
   ```bash
   docker image prune -a
   ```

### Task 45: Run contaiNERD with custom command

1. **Run contaiNERD with different command**:
   ```bash
   docker run -it node:18-alpine sh
   ```

2. **Execute commands inside contaiNERD**:
   ```bash
   # Inside the contaiNERD
   node --version
   npm --version
   exit
   ```

---

## 🔗 Section 4: Workflow Integration (5 Tasks)

### Task 46: Init Git + Docker project from scratch

1. **Create new project directory**:
   ```bash
   mkdir integrated-project
   cd integrated-project
   ```

2. **Initialize Git**:
   ```bash
   git init
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```

3. **Create basic project structure**:
   ```bash
   mkdir src
   mkdir tests
   touch README.md
   touch .gitignore
   touch .dockerignore
   ```

### Task 47: Write Dockerfile and .gitignore together

1. **Create .gitignore**:
   ```bash
   cat > .gitignore << EOF
   # Dependencies
   node_modules/
   npm-debug.log*
   
   # Environment variables
   .env
   .env.local
   
   # IDE files
   .vscode/
   .idea/
   
   # OS files
   .DS_Store
   Thumbs.db
   
   # Logs
   logs/
   *.log
   
   # Docker
   .dockerignore
   Dockerfile
   docker-compose.yml
   EOF
   ```

2. **Create Dockerfile**:
   ```bash
   cat > Dockerfile << EOF
   FROM node:18-alpine
   
   WORKDIR /app
   
   COPY package*.json ./
   RUN npm install
   
   COPY . .
   
   EXPOSE 3000
   
   CMD ["npm", "start"]
   EOF
   ```

3. **Create package.json**:
   ```bash
   cat > package.json << EOF
   {
     "name": "integrated-project",
     "version": "1.0.0",
     "description": "Git + Docker integrated project",
     "main": "src/app.js",
     "scripts": {
       "start": "node src/app.js",
       "test": "echo \"No tests specified\" && exit 0"
     },
     "dependencies": {
       "express": "^4.18.2"
     }
   }
   EOF
   ```

4. **Create .dockerignore**:
   ```bash
   cat > .dockerignore << EOF
   node_modules
   npm-debug.log
   .git
   .gitignore
   README.md
   .env
   .dockerignore
   Dockerfile
   docker-compose.yml
   tests
   EOF
   ```

### Task 48: Run contaiNERD and test output

1. **Create the application**:
   ```bash
   mkdir -p src
   cat > src/app.js << EOF
   const express = require('express');
   const app = express();
   const port = process.env.PORT || 3000;
   
   app.get('/', (req, res) => {
     res.json({
       message: 'Integrated Git + Docker project is running!',
       timestamp: new Date().toISOString(),
       environment: process.env.NODE_ENV || 'development'
     });
   });
   
   app.get('/health', (req, res) => {
     res.json({ status: 'healthy', uptime: process.uptime() });
   });
   
   app.listen(port, () => {
     console.log(\`Server running on port \${port}\`);
   });
   EOF
   ```

2. **Build and run contaiNERD**:
   ```bash
   docker build -t integrated-project .
   docker run -p 3000:3000 integrated-project
   ```

3. **Test the application**:
   ```bash
   curl http://localhost:3000
   curl http://localhost:3000/health
   ```

### Task 49: Push project to GitHub

1. **Add and commit files**:
   ```bash
   git add .
   git commit -m "Initial commit: Integrated Git + Docker project"
   ```

2. **Create GitHub repository**:
   - Go to GitHub and create a new repository named "integrated-project"
   - Don't initialize with README

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/your-username/integrated-project.git
   git push -u origin main
   ```

### Task 50: Clone repo on another PC and run

1. **Simulate cloning on another machine**:
   ```bash
   cd ..
   git clone https://github.com/your-username/integrated-project.git integrated-project-clone
   cd integrated-project-clone
   ```

2. **Install dependencies and run locally**:
   ```bash
   npm install
   npm start
   ```

3. **Or run with Docker**:
   ```bash
   docker build -t integrated-project .
   docker run -p 3000:3000 integrated-project
   ```

---

## 🎉 Completion Checklist

### Cursor Setup (11/11) ✅
- [ ] Install Cursor and sign in with GitHub
- [ ] Open a project folder in Cursor
- [ ] Use built-in terminal in Cursor
- [ ] Install one Cursor extension
- [ ] Create index.html and style.css
- [ ] Write a JS console.log() program
- [ ] Use AI autocomplete in Cursor
- [ ] Ask Cursor to explain code
- [ ] Format code with keyboard shortcut
- [ ] Create a README.md in markdown

### Git Fundamentals (18/18) ✅
- [ ] Install Git and set up user config
- [ ] Run git init in a project
- [ ] Add files with git add .
- [ ] Commit with git commit -m
- [ ] Check git status
- [ ] View history with git log
- [ ] Create .gitignore
- [ ] Create new branch feature/test
- [ ] Switch to another branch
- [ ] Merge branches
- [ ] Resolve a merge conflict
- [ ] Connect to GitHub (HTTPS/SSH)
- [ ] Push local repo to GitHub
- [ ] Pull remote changes
- [ ] Create a new branch and push it
- [ ] Clone repository on another location
- [ ] Fetch and merge changes
- [ ] Stash changes

### Docker Basics (16/16) ✅
- [ ] Install Docker
- [ ] Check Docker version
- [ ] Create a Dockerfile for Node app
- [ ] Build Docker image
- [ ] Run Docker contaiNERD
- [ ] View running contaiNERDs docker ps
- [ ] Stop/remove contaiNERD
- [ ] Create .dockerignore
- [ ] Add .env and use in contaiNERD
- [ ] Expose port 3000
- [ ] Use docker-compose
- [ ] Pull Docker image from DockerHub
- [ ] Tag & push image to DockerHub
- [ ] View logs with docker logs
- [ ] Remove image with docker rmi
- [ ] Run contaiNERD with custom command

### Workflow Integration (5/5) ✅
- [ ] Init Git + Docker project from scratch
- [ ] Write Dockerfile and .gitignore together
- [ ] Run contaiNERD and test output
- [ ] Push project to GitHub
- [ ] Clone repo on another PC and run

---

## 🚀 Next Steps

Congratulations! You've completed all 50 tasks in the NERD Dev Onboarding Sprint Week 1. Here's what you've accomplished:

### Skills Acquired
- **IDE Mastery**: Proficient with Cursor IDE and AI-assisted coding
- **Version Control**: Complete Git workflow from local to remote
- **Containerization**: Docker fundamentals and best practices
- **Workflow Integration**: Combining multiple tools effectively

### Portfolio Projects Created
1. **Basic Web Project**: HTML, CSS, JavaScript with proper documentation
2. **Node.js Docker App**: ContaiNERDized web application
3. **Integrated Project**: Complete Git + Docker workflow demonstration

### Professional Development Practices
- Code formatting and documentation
- Version control with branching and merging
- Contaier-based development
- CI/CD pipeline understanding
- Security best practices (.gitignore, .dockerignore)

### What to Do Next
1. **Continue Learning**: Explore advanced Git features, Docker networking, and multi-stage builds
2. **Build More Projects**: Apply these skills to real-world applications
3. **Contribute to Open Source**: Use your Git skills to contribute to projects
4. **Learn CI/CD**: Explore GitHub Actions, GitLab CI, or Jenkins
5. **Study DevOps**: Learn about infrastructure as code, monitoring, and deployment strategies

### Resources for Further Learning
- **Git**: [Git Documentation](https://git-scm.com/doc)
- **Docker**: [Docker Documentation](https://docs.docker.com/)
- **Node.js**: [Node.js Documentation](https://nodejs.org/docs/)
- **Cursor**: [Cursor Documentation](https://cursor.sh/docs)

---

**Remember**: The key to becoming a great developer is consistent practice. Use these tools daily, and they'll become second nature. Good luck with your development journey! 🚀