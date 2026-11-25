from a2a.types import AgentSkill, AgentCard

skill = AgentSkill(
    id="website_builder_simple_skill",
    name="website_builder_simple_skill",
    description="A simple website builder agent that can create basic web pages",
    tags=["website", "css", "javascript", "html"],
    examples=[
        "Create a simple webpage with a header and footer",
        "Create a landing page for a product with a call to action button"
    ]
)

agent_card = AgentCard(
    name="website_builder_simple",
)