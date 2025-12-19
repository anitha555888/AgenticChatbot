import streamlit as st
from src.langgrapagentiai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgrapagentiai.LLMS.groqllm import GroqLLM
from src.langgrapagentiai.graph.graph_builder import GraphBuilder
from src.langgrapagentiai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Docstring for load_langgraph_agenticai_app
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
       st.error("Error: Failed to load user input from the UI.")
       return
    
    user_message = st.chat_input("Enter your message:")
    
    if user_message:
       try:
          obj_llm_config = GroqLLM(user_input)
          model = obj_llm_config.get_llm_models()

          if not model:
             st.error("LLM model cannot be initialized")
             return
          
          usecase=user_input.get("selected_usecases")

          if not usecase:
             st.error("Error: no usecase selected")

          graphBuilder=GraphBuilder(model)
          try:
             graph = graphBuilder.setup_graph(usecase)
             DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
          except Exception as e:
             st.error(f"Error: graph setup failed. {e}")
             return
          
       except Exception as e:
             st.error(f"Error: {e}")
             return