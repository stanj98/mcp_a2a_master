from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

class ArithmeticInput(BaseModel):
    a: float = Field(..., description="First Number")
    b: float = Field(..., description="Second Number")
   
class ArithmeticOutput(BaseModel):
    result: float = Field(..., description="Result of the arithmetic operation")
    expression: str = Field(..., description="Expression evaluated")
    
mcp = FastMCP(
    "arithemtic_server",
    host="localhost",
    port=8000,
    stateless_http = True
)