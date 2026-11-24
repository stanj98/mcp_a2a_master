from utilities.common.file_loader import load_instructions_file
from google.adk.agents import LlmAgent

class website_builder_simple:
    """
    A simple website builder agent that can create basic web pages and is built using
    Google's agent development framework.
    """
    
    def __init__(self):
        self.system_instruction = load_instructions_file("agents/website_builder_simple/instructions.txt")
        self.description = load_instructions_file("agents/website_builder_simple/description.txt")
    
    def _build_agent(self) -> LlmAgent:
        return LlmAgent(
            name="website_builder_simple",
            model="gemini-2.0-flash",
            instruction=self.system_instruction,
            description=self.description,
        )
    