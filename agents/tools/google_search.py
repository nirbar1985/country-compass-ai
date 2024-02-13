from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper


@tool
def google_search(query: str):
    """Performs a Google search using the provided query string. Choose this tool when you need to find current data"""
    return SerpAPIWrapper().run(query)
