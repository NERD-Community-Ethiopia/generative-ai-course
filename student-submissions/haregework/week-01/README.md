# Week 1 Assignment: Environment Setup & Social Network Simulation

## 📋 Project Title
Environment Setup and Python Social Network Simulation using NetworkX

## 📝 Description
This project demonstrates the successful setup of the development environment for the Generative AI & Automation course and implements a simple social network simulation using Python's NetworkX library. The simulation creates a network of users, simulates interactions, and analyzes network properties.

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Git
- pip (Python package installer)

### Step-by-Step Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/generative-ai-course.git
   cd generative-ai-course
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install networkx matplotlib numpy
   ```

4. **Verify Installation**
   ```bash
   python -c "import networkx as nx; print('NetworkX installed successfully!')"
   ```

## 🚀 Usage

### Running the Social Network Simulation

1. **Navigate to the assignment directory**
   ```bash
   cd student-submissions/haymanot/week-01
   ```

2. **Run the simulation**
   ```bash
   python social_network_simulation.py
   ```

3. **View the generated network visualization**
   - The script will create a `network_visualization.png` file
   - Network statistics will be printed to the console

### Example Output
```
Social Network Simulation Results:
================================
Total Users: 20
Total Connections: 45
Average Degree: 4.5
Network Density: 0.237
Connected Components: 1
Average Path Length: 2.1
Network visualization saved as: network_visualization.png
```

## 📦 Dependencies

### Required Packages
- `networkx==3.1` - Network analysis and visualization
- `matplotlib==3.7.1` - Plotting and visualization
- `numpy==1.24.3` - Numerical computations
- `requests==2.31.0` - HTTP library for API calls
- `python-dotenv==1.0.0` - Environment variable management

### Installation Command
```bash
pip install networkx matplotlib numpy requests python-dotenv
```

## 📊 Output

### Expected Results
1. **Console Output**: Network statistics including:
   - Number of users and connections
   - Average degree and network density
   - Connected components analysis
   - Average path length

2. **Visual Output**: 
   - `network_visualization.png` - Network graph visualization
   - `network_analysis.txt` - Detailed analysis report

3. **Network Properties**:
   - Scale-free network characteristics
   - Community detection results
   - Centrality measures for key nodes

## 🎯 Challenges Encountered

### 1. Environment Setup
- **Challenge**: Virtual environment activation issues on Windows
- **Solution**: Used `venv\Scripts\activate` instead of `source venv/bin/activate`

### 2. NetworkX Installation
- **Challenge**: Package conflicts with existing Python installation
- **Solution**: Created isolated virtual environment and installed packages fresh

### 3. Network Visualization
- **Challenge**: Matplotlib backend issues on Windows
- **Solution**: Used `matplotlib.use('Agg')` for non-interactive plotting

### 4. Git Configuration
- **Challenge**: Initial Git setup and branch creation
- **Solution**: Followed the course Git workflow guidelines

## 📚 Learning Outcomes

### Technical Skills Gained
1. **Environment Management**: Learned to set up isolated Python environments
2. **Network Analysis**: Understanding of graph theory and network properties
3. **Data Visualization**: Creating meaningful network visualizations
4. **Git Workflow**: Proper version control practices for collaborative development

### Concepts Understood
1. **Social Network Theory**: How networks form and evolve
2. **Network Metrics**: Degree, density, centrality, and path length
3. **Scale-Free Networks**: Power-law degree distributions
4. **Community Detection**: Identifying clusters within networks

### Development Practices
1. **Documentation**: Writing comprehensive README files
2. **Code Organization**: Structuring projects with proper file organization
3. **Version Control**: Using Git for project management
4. **Testing**: Verifying code functionality before submission

## 🔧 Code Structure

```
student-submissions/haymanot/week-01/
├── README.md                    # This file
├── social_network_simulation.py # Main simulation code
├── requirements.txt             # Python dependencies
├── network_visualization.png   # Generated network graph
└── network_analysis.txt        # Detailed analysis report
```

## 🎓 Next Steps

1. **Week 2 Preparation**: Understanding ML workflows and prompt engineering
2. **Advanced Network Analysis**: Implementing more complex network algorithms
3. **Integration with AI**: Combining network analysis with machine learning
4. **API Development**: Creating web services for network analysis

## 📞 Support

For questions or issues:
- **Discord**: [Course Support Channel](https://discord.gg/WBwr3F4y)
- **GitHub Issues**: Create an issue in the main repository
- **Office Hours**: Check course schedule for instructor availability

---

*This assignment demonstrates the successful setup of the development environment and provides a foundation for more advanced AI and automation projects in the coming weeks.* 