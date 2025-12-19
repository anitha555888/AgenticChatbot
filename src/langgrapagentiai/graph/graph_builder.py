from langgraph.graph import StateGraph, START,END
from src.langgrapagentiai.state.state import State
from src.langgrapagentiai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgrapagentiai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgrapagentiai.nodes.chatbot_with_tool_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Docstring for basic_chatbot_build_graph
        
        :param self: Description
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    def chat_with_tools_build_graph(self):
        """
        Docstring for chat_with_tools_build_graph
        
        :param self: Description
        """
        llm=self.llm
        tools=get_tools()
        tools_node=create_tool_node(tools)
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
   
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

     
        
        
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tools_node)
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
       # self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """
        Docstring for setup_graph
        
        :param self: Description
        :param usecase: Description
        :type usecase: str
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()
        if usecase == "Chatbot with Web":
           self.chat_with_tools_build_graph()
           return self.graph_builder.compile()
        