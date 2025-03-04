#!/usr/bin/env python
"""
Simple script to build and run Adam-o1 Docker containers.
"""

import os
import subprocess
import platform
import time
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and print output in real-time."""
    print(f"Running: {' '.join(command)}")
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=False,  
        cwd=cwd
    )
    
    for line in process.stdout:
        try:
            decoded_line = line.decode('utf-8', errors='replace')
            print(decoded_line.strip())
        except Exception as e:
            print(f"Error processing output: {e}")
    
    process.wait()
    return process.returncode

def check_docker():
    """Check if Docker is installed and running."""
    try:
        subprocess.run(
            ["docker", "--version"], 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: Docker is not installed or not in PATH")
        return False

def main():
    """Main function to build and run Adam-o1 containers."""
    # Check if Docker is available
    if not check_docker():
        return 1
    
    # Get the base directory
    base_dir = Path(__file__).parent.absolute()
    
    # Check for .env file
    env_file = base_dir / ".env"
    env_args = []
    if env_file.exists():
        print(f"Using environment file: {env_file}")
        env_args = ["--env-file", str(env_file)]
    else:
        print("No .env file found. Continuing without environment variables.")
    
    # Build the MCP container
    print("\n=== Building Adam-o1 MCP container ===")
    mcp_dir = base_dir / "mcp"
    if run_command(["docker", "build", "-t", "adam-o1-mcp:latest", "."], cwd=mcp_dir) != 0:
        print("Error building MCP container")
        return 1
    
    # Build the main Adam-o1 container
    print("\n=== Building main Adam-o1 container ===")
    if run_command(["docker", "build", "-t", "adam-o1:latest", "."], cwd=base_dir) != 0:
        print("Error building main Adam-o1 container")
        return 1
    
    # Check if the container is already running
    try:
        result = subprocess.run(
            ["docker", "ps", "-q", "--filter", "name=adam-o1-container"],
            check=True,
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            print("\n=== Stopping existing Adam-o1 container ===")
            run_command(["docker", "stop", "adam-o1-container"])
            run_command(["docker", "rm", "adam-o1-container"])
    except subprocess.SubprocessError:
        pass
    
    # Run the Adam-o1 container
    print("\n=== Starting Adam-o1 container ===")
    cmd = [
        "docker", "run", "-d",
        "--name", "adam-o1-container",
        "-p", "8501:8501",
        "-p", "8100:8100",
        "--add-host", "host.docker.internal:host-gateway"
    ]
    
    # Add environment variables if .env exists
    if env_args:
        cmd.extend(env_args)
    
    # Add image name
    cmd.append("adam-o1:latest")
    
    if run_command(cmd) != 0:
        print("Error starting Adam-o1 container")
        return 1
    
    # Wait a moment for the container to start
    time.sleep(2)
    
    # Print success message
    print("\n=== Adam-o1 is now running! ===")
    print("-> Access the Streamlit UI at: http://localhost:8501")
    print("-> MCP container is ready to use - see the MCP tab in the UI.")
    print("\nTo stop Adam-o1, run: docker stop adam-o1-container && docker rm adam-o1-container")
    
    return 0

if __name__ == "__main__":
    exit(main())
