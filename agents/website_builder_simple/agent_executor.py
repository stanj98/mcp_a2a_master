from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from agents.website_builder_simple.agent import WebsiteBuilderSimple

class WebsiteBuilderSimpleAgentExecutor(AgentExecutor):
    """ 
    Implements the AgentExecutor interface to integrate the
    website builder simple agent with the A2A framework.
    """
    
    def __init__(self):
        self.agent = WebsiteBuilderSimple()
        
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        llm_agent = self.agent._build_agent()
        return await llm_agent.execute(context, event_queue)