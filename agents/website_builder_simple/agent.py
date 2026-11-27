from utilities.common.file_loader import load_instructions_file
from collections.abc import AsynIterable
from google.adk.agents import LlmAgent
from google.adk import Runner
from googe.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.adk.in_memory_memory_service import InMemoryMemoryService
from google.genai import types

class website_builder_simple:
    """
    A simple website builder agent that can create basic web pages and is built using
    Google's agent development framework.
    """
    
    def __init__(self):
        self.system_instruction = load_instructions_file("agents/website_builder_simple/instructions.txt")
        self.description = load_instructions_file("agents/website_builder_simple/description.txt")
        self._agent = self._build_agent()
        self._user_id = "website_builder_simple_agent_user"
        self._runner = Runner(
            app_name = self._agent_name,
            agent = self._agent,
            artifact_service = InMemoryArtifactService(),
            session_service = InMemorySessionService(),
            memory_service = InMemoryMemoryService()
        )

    
    def _build_agent(self) -> LlmAgent:
        return LlmAgent(
            name="website_builder_simple",
            model="gemini-2.0-flash",
            instruction=self.system_instruction,
            description=self.description,
        )
    
    async def invoke(self, query: str, session_id: str) -> AsynIterable[dict]:
        """
        Invoke the agent
        Return the stream of updates back to the caller as the agent processes the query

        {
            'is_task_complete': bool, #indicates if the task is complete
            updates: str, #updates on the task progress
            content: str, $Final result of the task is complete
        }
        """
        session = await self._runner.session_service.get_session(
            app_name = self._agent_name,
            session_id= session_id,
            user_id = self._user_id
        )

        if not session:
            session = await self._runner.session_service.create_session(
                app_name = self._agent_name,
                session_id= session_id,
                user_id = self._user_id
            )

        user_content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=query)]
        )

        async for event in self._runner.run_async(
            user_id = self._user_id,
            session_id= session_id,
            new_message = user_content
        ):
            if event.is_final_response:
                final_response = ""
                if event.content and event.content.parts and event.content.parts[-1].text:
                    final_response = event.content.parts[-1].text
            
                yield {
                    'is_task_complete': True,
                    'updates': "Task completed succesfully",
                    "content": final_response
                }
            else:
                yield {
                    'is_task_complete': False,
                    'updates': "Agent is processing your request"
                }
