# Setup script for AutoGPT on Windows
# Run this script with administrator privileges

# Function to check if a command exists
function Test-CommandExists {
    param ($command)
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = 'stop'
    try {
        if (Get-Command $command) { return $true }
    }
    catch { return $false }
    finally { $ErrorActionPreference = $oldPreference }
}

# Function to check minimum Python version
function Test-PythonVersion {
    param ($minVersion)
    try {
        $pythonVersion = (python --version 2>&1).ToString().Split(" ")[1]
        $currentVersion = [version]$pythonVersion
        $minimumVersion = [version]$minVersion
        return $currentVersion -ge $minimumVersion
    }
    catch {
        return $false
    }
}

# Function to check if running as administrator
function Test-Administrator {
    $user = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($user)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Check if running as administrator
if (-not (Test-Administrator)) {
    Write-Host "Please run this script as Administrator!" -ForegroundColor Red
    exit 1
}

Write-Host "[*] Checking prerequisites..." -ForegroundColor Cyan

# Check Python
if (-not (Test-CommandExists python)) {
    Write-Host "[X] Python is not installed. Please install Python 3.10 or higher from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}
elseif (-not (Test-PythonVersion "3.10")) {
    Write-Host "[X] Python version must be 3.10 or higher" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "[+] Python installation verified" -ForegroundColor Green
}

# Check pip
if (-not (Test-CommandExists pip)) {
    Write-Host "[X] pip is not installed or not in PATH" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "[+] pip installation verified" -ForegroundColor Green
}

# Check Git
if (-not (Test-CommandExists git)) {
    Write-Host "[X] Git is not installed. Please install from https://git-scm.com/download/win" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "[+] Git installation verified" -ForegroundColor Green
}

# Check Node.js
if (-not (Test-CommandExists node)) {
    Write-Host "[X] Node.js is not installed. Please install from https://nodejs.org/" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "[+] Node.js installation verified" -ForegroundColor Green
}

# Check Docker
if (-not (Test-CommandExists docker)) {
    Write-Host "[X] Docker is not installed. Please install Docker Desktop from https://www.docker.com/products/docker-desktop/" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "[+] Docker installation verified" -ForegroundColor Green
}

# Setup virtual environment
Write-Host "`n[*] Setting up Python virtual environment..." -ForegroundColor Cyan

# Remove existing venv if it exists
if (Test-Path "venv") {
    Write-Host "Removing existing virtual environment..."
    Remove-Item -Recurse -Force "venv"
}

try {
    # Create new virtual environment
    python -m venv venv
    Write-Host "[+] Virtual environment created" -ForegroundColor Green

    # Activate virtual environment
    Write-Host "Activating virtual environment..."
    .\venv\Scripts\Activate

    # Upgrade pip in virtual environment
    Write-Host "Upgrading pip..."
    python -m pip install --upgrade pip

    # Install requirements if requirements.txt exists
    if (Test-Path "requirements.txt") {
        Write-Host "Installing requirements..."
        pip install -r requirements.txt
        Write-Host "[+] Requirements installed" -ForegroundColor Green
    }
    else {
        Write-Host "[!] requirements.txt not found" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "[X] Error during virtual environment setup: $_" -ForegroundColor Red
    exit 1
}

# Set execution policy for virtual environment
Write-Host "`n[*] Setting execution policy for virtual environment..." -ForegroundColor Cyan
try {
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Write-Host "[+] Execution policy set" -ForegroundColor Green
}
catch {
    Write-Host "[X] Error setting execution policy: $_" -ForegroundColor Red
}

Write-Host "`n[+] Setup completed successfully!" -ForegroundColor Green
Write-Host "To activate the virtual environment in a new terminal, run: .\venv\Scripts\Activate" -ForegroundColor Yellow
Write-Host "To deactivate the virtual environment, run: deactivate" -ForegroundColor Yellow 