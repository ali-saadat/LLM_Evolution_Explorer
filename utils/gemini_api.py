"""
Gemini API integration for the LLM Evolution Explorer application.
"""
import google.generativeai as genai
from utils.config import get_config

def initialize_gemini():
    """
    Initialize the Gemini API with the API key from configuration.
    
    Returns:
        bool: True if initialization was successful, False otherwise.
    """
    config = get_config()
    api_key = config["gemini_api_key"]
    
    if not api_key:
        return False
    
    try:
        genai.configure(api_key=api_key)
        # Test if we can list models
        genai.list_models()
        return True
    except Exception as e:
        print(f"Error initializing Gemini API: {str(e)}")
        return False

def get_available_models():
    """
    Get the list of available Gemini models.
    
    Returns:
        list: List of available model names.
    """
    try:
        models = [model.name for model in genai.list_models() 
                 if "generateContent" in model.supported_generation_methods]
        return models
    except Exception:
        # Return default models if API call fails
        return get_config()["available_models"]

def generate_response(prompt, model_name=None):
    """
    Generate a response from Gemini for a given prompt.
    
    Args:
        prompt (str): The prompt to send to Gemini.
        model_name (str, optional): The model to use. Defaults to None, which uses the default model.
    
    Returns:
        str: The generated response.
    """
    if not model_name:
        model_name = get_config()["default_model"]
    
    # Try with the specified model first
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        print(f"Error with model {model_name}: {error_msg}")
        
        # If the specified model fails, try other available models
        if "not found" in error_msg or "not supported" in error_msg:
            available_models = get_config()["available_models"]
            for alt_model in available_models:
                if alt_model != model_name:
                    try:
                        print(f"Trying alternative model: {alt_model}")
                        model = genai.GenerativeModel(alt_model)
                        response = model.generate_content(prompt)
                        return f"[Using model: {alt_model}] " + response.text
                    except Exception as alt_e:
                        print(f"Error with alternative model {alt_model}: {str(alt_e)}")
        
        return f"Error generating response: {error_msg}. Please try a different model or check your API key."

def generate_rag_response(prompt, context, model_name=None):
    """
    Generate a RAG-enhanced response from Gemini for a given prompt and context.
    
    Args:
        prompt (str): The prompt to send to Gemini.
        context (str): The context to use for RAG.
        model_name (str, optional): The model to use. Defaults to None, which uses the default model.
    
    Returns:
        str: The generated response.
    """
    if not model_name:
        model_name = get_config()["default_model"]
    
    # Create a RAG-enhanced prompt
    rag_prompt = f"""
    Context information:
    {context}
    
    Based on the above context, please answer the following question:
    {prompt}
    
    If the answer is not in the context, please say so. When using information from the context, cite the relevant parts.
    """
    
    # Try with the specified model first
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(rag_prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        print(f"Error with model {model_name} for RAG: {error_msg}")
        
        # If the specified model fails, try other available models
        if "not found" in error_msg or "not supported" in error_msg:
            available_models = get_config()["available_models"]
            for alt_model in available_models:
                if alt_model != model_name:
                    try:
                        print(f"Trying alternative model for RAG: {alt_model}")
                        model = genai.GenerativeModel(alt_model)
                        response = model.generate_content(rag_prompt)
                        return f"[Using model: {alt_model}] " + response.text
                    except Exception as alt_e:
                        print(f"Error with alternative model {alt_model} for RAG: {str(alt_e)}")
        
        return f"Error generating RAG response: {error_msg}. Please try a different model or check your API key."
