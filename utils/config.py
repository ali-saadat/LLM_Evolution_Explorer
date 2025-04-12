"""
Configuration utilities for the LLM Evolution Explorer application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Default configuration
DEFAULT_CONFIG = {
    "app_title": "LLM Evolution Explorer",
    "app_description": "Explore the evolution of LLMs — from basic queries to agentic RAG integrations",
    "gemini_api_key": os.getenv("GEMINI_API_KEY", ""),
    "default_model": "gemini-1.5-pro",
    "available_models": ["gemini-1.5-pro", "gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-1.5-flash"],
    "github_repo": "https://github.com/modelcontextprotocol/python-sdk",
    "temp_folder": "/tmp/llm_evolution_explorer",
}

# Ensure temp folder exists
os.makedirs(DEFAULT_CONFIG["temp_folder"], exist_ok=True)

def get_config():
    """
    Get the application configuration.
    
    Returns:
        dict: The application configuration.
    """
    return DEFAULT_CONFIG

def save_api_key(api_key):
    """
    Save the Gemini API key to the configuration.
    
    Args:
        api_key (str): The Gemini API key.
    """
    DEFAULT_CONFIG["gemini_api_key"] = api_key
