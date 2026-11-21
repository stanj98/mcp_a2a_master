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
    port=3000,
    stateless_http = True,
)

@mcp.tool("add_numbers")
async def add_numbers(input: ArithmeticInput) -> ArithmeticOutput:
    """
        Add two numbers and return the result.
        
        Args:
            input (ArithmeticInput): Input containing two numbers to add.
            
        Returns:
            ArithemticInput: Output containing the result and the expression evaluated.
    """
    result = input.a + input.b
    expression = f"{input.a} + {input.b} = {result}"
    return ArithmeticOutput(result=result, expression=expression) 