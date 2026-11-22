
class MCPDiscovery:
    """
    Reads a JSON config file defining MCP servers and provides access
    to the server definitions under the mcpServers key
    
    Attributes:
        config_file (str): Path to the JSON configuration file.
        config (Dict[str, Any]): Parsed JSON content, expected to contain the "mcpServers" key.
    """
    
    