# AutoGPT Windows 11 Setup Guide

This guide provides step-by-step instructions for setting up AutoGPT on Windows 11.

## Prerequisites

1. **System Requirements**
   - Windows 11 (64-bit)
   - At least 8GB RAM (16GB recommended)
   - At least 10GB free disk space
   - Internet connection

2. **Required Software**
   - Git
   - Python 3.10 or higher
   - Node.js (Latest LTS version)
   - Docker Desktop
   - Visual Studio Code
   - Windows Terminal (optional but recommended)

## Installation Steps

### 1. Install Required Software

#### Git Installation
1. Download Git from [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer, using default settings
3. Verify installation by opening Command Prompt and typing:
   ```bash
   git --version
   ```

#### Python Installation
1. Download Python 3.10 or higher from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   pip --version
   ```

#### Node.js Installation
1. Download Node.js LTS from [https://nodejs.org/](https://nodejs.org/)
2. Run the installer, using default settings
3. Verify installation:
   ```bash
   node --version
   npm --version
   ```

#### Docker Desktop Installation
1. Download Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. **IMPORTANT**: If you haven't enabled virtualization in BIOS, you'll need to do so
3. Install Docker Desktop
4. Start Docker Desktop and wait for it to fully load
5. Verify installation:
   ```bash
   docker --version
   ```

#### Visual Studio Code Installation
1. Download VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Run the installer
3. Recommended extensions to install:
   - Python
   - Docker
   - GitLens
   - Prettier

### 2. Setup AutoGPT

1. **Clone the Repository**
   ```bash
   cd C:\Users\YourUsername\Documents
   git clone https://github.com/Significant-Gravitas/AutoGPT.git
   cd AutoGPT
   ```

2. **Setup Python Environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Copy `.env.example` to `.env`
   - Open `.env` in VS Code
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

4. **Run Initial Setup**
   ```bash
   .\run setup
   ```

### 3. Running AutoGPT

1. **Start the Platform**
   ```bash
   .\run agent start
   ```
   This will start both the backend server and frontend interface.

2. **Access the Interface**
   - Open your web browser
   - Navigate to `http://localhost:3000`
   - You should see the AutoGPT interface

## Troubleshooting

### Common Issues and Solutions

1. **Python "not recognized" error**
   - Solution: Ensure Python is added to PATH
   - Open System Properties > Advanced > Environment Variables
   - Add Python and pip directories to Path

2. **Docker errors**
   - Ensure WSL 2 is installed and enabled
   - Run in PowerShell as administrator:
     ```powershell
     wsl --install
     ```
   - Restart your computer

3. **Port conflicts**
   - If ports 3000 or 8000 are in use:
     ```bash
     netstat -ano | findstr :3000
     netstat -ano | findstr :8000
     ```
   - Stop the conflicting process or change the port in configuration

4. **Virtual Environment Issues**
   - If `venv` activation fails, try:
     ```bash
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

### Getting Help

1. Check the [official documentation](https://docs.agpt.co)
2. Join the [Discord community](https://discord.gg/autogpt)
3. Search [GitHub Issues](https://github.com/Significant-Gravitas/AutoGPT/issues)

## Updating AutoGPT

To update to the latest version:

```bash
git pull origin master
.\venv\Scripts\activate
pip install -r requirements.txt
.\run setup
```

## Security Notes

1. Never share your `.env` file or API keys
2. Keep Docker Desktop and all dependencies updated
3. Use strong passwords for any accounts created
4. Monitor resource usage through Docker Desktop

## Additional Tips

1. Use Windows Terminal for a better command-line experience
2. Consider using WSL 2 for a Linux-like development environment
3. Regular backups of your configurations are recommended
4. Keep track of your API usage if using OpenAI keys 