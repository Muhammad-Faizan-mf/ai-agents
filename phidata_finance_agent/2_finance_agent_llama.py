"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str)-> str:
    """Function to get the symbol of company.

    Args:
        company (str): The name of the company.
    
    Returns:
        str: The symbol of the company.
    """

    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }
    return symbols.get(company,"Unknown")


agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals= True), get_company_symbol],
    instructions = [
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    show_tools_calls = True,
    markdown = True,
    debug_mode = True,
)


agent.print_response(
        "Summarize and compare analyst recommendations and fundamentals for TSLA and MSFT. Show in tables.", stream=True
)