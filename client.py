# simplified_wsl_client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import time

async def main():
    # Define server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["wsl_automation_server.py"],
    )

    # Connect to the server
    print("Connecting to WSL Automation server...")
    try:
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                # Initialize the connection
                await session.initialize()
                
                print("\n=== Simple WSL Automation ===")
                
                wsl_opened = False
                
                while True:
                    print("\n" + "="*40)
                    print("OPTIONS MENU:")
                    print("="*40)
                    print("1. Open WSL terminal")
                    print("2. Run command in WSL")
                    print("3. List common Linux commands")
                    print("4. Close WSL session (if you manually closed the window)")
                    print("5. Exit")
                    print("="*40)
                    
                    choice = input("Select option (1-5): ").strip()
                    
                    if choice == "1":
                        # Open WSL
                        print("\nOpening WSL terminal...")
                        result = await session.call_tool("open_wsl")
                        print(f"Result: {result.content[0].text}")
                        wsl_opened = True
                        
                    elif choice == "2":
                        # Make sure WSL is open first
                        if not wsl_opened:
                            print("\nOpening WSL terminal first...")
                            result = await session.call_tool("open_wsl")
                            print(f"Result: {result.content[0].text}")
                            wsl_opened = True
                            time.sleep(1)
                        
                        # Get the command to run
                        command = input("\nENTER WSL COMMAND: ").strip()
                        
                        # Send the command
                        result = await session.call_tool("send_to_wsl", arguments={"command": command})
                        print(f"Result: {result.content[0].text}")
                        
                        # Ask if user wants to run another command
                        while True:
                            print("\n" + "="*40)
                            another = input("Run another command? (Enter Y/N): ").strip().lower()
                            print("="*40 + "\n")
                            
                            if another != 'y':
                                break
                                
                            command = input("ENTER WSL COMMAND: ").strip()
                            result = await session.call_tool("send_to_wsl", arguments={"command": command})
                            print(f"Result: {result.content[0].text}")
                    
                    elif choice == "3":
                        result = await session.call_tool("list_linux_commands")
                        print(f"\n{result.content[0].text}")
                    
                    elif choice == "4":
                        # Mark WSL as closed (if user manually closed the window)
                        result = await session.call_tool("close_wsl")
                        print(f"Result: {result.content[0].text}")
                        wsl_opened = False
                    
                    elif choice == "5":
                        print("Exiting...")
                        break
                    
                    else:
                        print("Invalid option. Please try again.")
                    
                    input("\nPress ENTER to return to menu...")
                    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())