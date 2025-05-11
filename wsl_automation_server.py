# wsl_automation_server.py
from mcp.server.fastmcp import FastMCP
import subprocess
import time
import pyautogui

# Create an MCP server
mcp = FastMCP("wsl_automation_server")

# Global variable to track if WSL is already open
wsl_is_open = False

@mcp.tool()
def open_wsl() -> str:
    """Open the Windows Subsystem for Linux (WSL) terminal and click on it if not already open"""
    global wsl_is_open
    
    try:
        if not wsl_is_open:
            # Open WSL terminal
            subprocess.Popen('cmd.exe /c start wsl.exe -d Ubuntu -e bash -c "cd /home/ahmad && bash"', shell=True)
            time.sleep(2)  # Wait for it to open
            
            # Find center of screen to click on WSL window
            screen_width, screen_height = pyautogui.size()
            center_x = screen_width // 2
            center_y = screen_height // 2
            
            # Click in the middle of the screen (where WSL window should be)
            pyautogui.click(center_x, center_y)
            
            wsl_is_open = True
            return "WSL terminal opened and clicked in the middle"
        else:
            # Just focus the existing WSL window
            screen_width, screen_height = pyautogui.size()
            center_x = screen_width // 2
            center_y = screen_height // 2
            
            # Click in the middle of the screen (where WSL window should be)
            pyautogui.click(center_x, center_y)
            
            return "WSL terminal is already open and now focused"
    except Exception as e:
        return f"Error opening WSL: {str(e)}"

@mcp.tool()
def send_to_wsl(command: str) -> str:
    """Send a command to the WSL window
    
    Args:
        command: Linux command to run
    """
    global wsl_is_open
    
    try:
        # If WSL isn't open yet, open it first
        if not wsl_is_open:
            open_wsl()
        else:
            # Click in the middle of the screen to focus WSL
            screen_width, screen_height = pyautogui.size()
            pyautogui.click(screen_width // 2, screen_height // 2)
            time.sleep(0.5)
        
        # Type the command
        pyautogui.write(command)
        time.sleep(0.2)
        
        # Press Enter
        pyautogui.press('enter')
        
        return f"Command '{command}' sent to WSL"
    except Exception as e:
        return f"Error sending command: {str(e)}"

@mcp.tool()
def close_wsl() -> str:
    """Mark WSL as closed (for use when manually closing the WSL window)"""
    global wsl_is_open
    wsl_is_open = False
    return "WSL marked as closed"

@mcp.tool()
def list_linux_commands() -> str:
    """List common Linux commands that can be used in WSL"""
    commands = {
        "Navigation": {
            "ls": "List directory contents",
            "cd [directory]": "Change to directory",
            "pwd": "Print working directory"
        },
        "File Operations": {
            "cp [source] [dest]": "Copy files",
            "mv [source] [dest]": "Move/rename files",
            "rm [file]": "Remove files",
            "mkdir [directory]": "Create directory",
            "touch [file]": "Create empty file",
            "cat [file]": "Display file contents"
        },
        "System Info": {
            "uname -a": "System information",
            "df -h": "Disk space usage",
            "free -m": "Memory usage"
        }
    }
    
    result = "Common Linux Commands for WSL:\n\n"
    for category, cmds in commands.items():
        result += f"=== {category} ===\n"
        for cmd, desc in cmds.items():
            result += f"{cmd}: {desc}\n"
        result += "\n"
    
    return result

# Run the server
if __name__ == "__main__":
    mcp.run()