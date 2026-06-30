from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Share 2 sentences between friends discussing on AI")