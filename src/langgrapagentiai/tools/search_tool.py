
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
import os

print(os.getenv("TAVILY_API_KEY"))

def get_tools():
    """
    Docstring for get_tools
    """
    tools=[TavilySearch(max_results=2,tavily_api_key="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")]
    return tools
def create_tool_node(tools):
    """
    Docstring for create_tool_node
    
    :param tools: Description
    """
    return ToolNode(tools=tools)
