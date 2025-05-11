# WSL Automation with MCP

A simple yet powerful tool to automate Windows Subsystem for Linux (WSL) operations using Python and the Model Control Protocol (MCP).

## Overview

This project provides a bridge between Windows and Linux environments by automating WSL interactions through a friendly menu-driven interface. It allows you to:

- Open WSL terminals programmatically
- Send commands to WSL without manual typing
- Get reference information for common Linux commands
- Integrate with AI assistants like Claude through MCP

## How It Works

The project consists of two main components:

1. **WSL Automation Server** (`wsl_automation_server.py`): Uses PyAutoGUI to control WSL windows and execute commands
2. **Client Application** (`client.py`): Provides a menu-driven interface to interact with the server

## Available Tools

The automation provides several tools through the MCP interface:

1. **open_wsl()**: Opens the WSL terminal and focuses it
2. **send_to_wsl(command)**: Sends a command to the WSL terminal
3. **close_wsl()**: Marks the WSL terminal as closed
4. **list_linux_commands()**: Provides a reference of common Linux commands

## Getting Started

### Prerequisites

- Python 3.6+
- Windows with WSL installed
- Required packages (see `requirements.txt`)


### Configuration

To integrate with Claude or other MCP-compatible AI assistants, add the following to your configuration:

```json
{
  "mcpServers": {
    "wsl_automation": {
      "command": "C:\\Users\\Name\\miniconda3\\envs\\mcp\\python.exe",
      "args": [
        "C:\\Users\\Name\\Desktop\\mcp_PyAutoGUI\\wsl_automation_server.py"
      ]
    }
  }
}
```

## Blog Post

For a detailed explanation of this project, check out my Medium post:
[Automating WSL with Python and Model Control Protocol (MCP)](https://medium.com/@ahmad.suliman011994/automating-wsl-with-python-and-model-control-protocol-mcp-4e5c2cc36b21) 



## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
