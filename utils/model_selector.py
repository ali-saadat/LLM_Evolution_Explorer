"""
Script to add model selection to the Streamlit app.
"""
import streamlit as st
from utils.gemini_api import get_available_models

def add_model_selector():
    """
    Add a model selector to the Streamlit sidebar.
    
    Returns:
        str: The selected model name.
    """
    # Get available models
    available_models = get_available_models()
    
    # Add model selector to sidebar
    st.sidebar.markdown("### Model Selection")
    st.sidebar.markdown("Select the Gemini model to use:")
    
    # Default to the first model in the list
    default_index = 0
    
    # Create the selector
    selected_model = st.sidebar.selectbox(
        "Model:",
        options=available_models,
        index=default_index,
        key="model_selector"
    )
    
    # Display model info
    st.sidebar.markdown(f"**Selected model:** {selected_model}")
    
    return selected_model
