from mcp.server.fastmcp import FastMCP  # pylint: disable=no-name-in-module
import os

mcp = FastMCP("terminal_server")
DEFAULT_WORKSPACE = os.path.expanduser("~/Documents/mcp_a2a_master/mcp/workspace")

@mcp.tool("terminal_server")
async def run_command(command: str) -> str:
    """
        Run a command in the terminal and return the output.
        Args:
            command(str): The command run in the terminal.
        Returns:
            str: The output of the command or an error message if the command fails.
    """
    import subprocess
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
        
    