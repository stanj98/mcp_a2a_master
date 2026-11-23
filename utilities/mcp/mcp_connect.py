
from utilities.mcp.mcp_discovery import MCPDiscovery
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from mcp import StdioServerParameters

class MCPConnector:
    
    """
    Discovers MCP servers from the config
    Config will be loaded by MCP discovery class
    then it lists each server's tools and then caches them as
    MCPToolSets that are compatible with Google's Agent Development Kit.
    """
    
    def __init__(self, config_file: str = None):
        self.discovery = MCPDiscovery(config_file=config_file)
        self.tools: list[MCPToolset] = []
        self._load_all_tools()
        
    async def _load_all_tools(self):
        """
        Loads all tools from discovered MCP servers and caches them as MCPToolSets.
        """
        for name, server in self.discovery.list_servers():
            if server.get("command") == "streamable_http":
                conn = StreamableHTTPServerParams(url=server["args"][0])
            else:
                conn = StdioConnectionParams(
                    server_params=StdioServerParameters(
                        command = server["command"],
                        args = server["args"]
                    ),
                    timeout=5
                )
            
        
    
    