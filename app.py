"""
Main Streamlit application for the LLM Evolution Explorer.
"""
import streamlit as st
import os
import sys

# Add the current directory to the path so imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.config import get_config, save_api_key
from utils.gemini_api import initialize_gemini, generate_response, generate_rag_response, get_available_models
from utils.document_processor import extract_text_from_pdf, save_uploaded_file
from utils.model_selector import add_model_selector
import asyncio

# Set page configuration
config = get_config()
st.set_page_config(
    page_title=config["app_title"],
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #e9f5ff;
        margin-bottom: 1rem;
        border-left: 4px solid #0096ff;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function."""
    # Initialize session state
    if "api_key_submitted" not in st.session_state:
        st.session_state.api_key_submitted = False
    if "current_setup" not in st.session_state:
        st.session_state.current_setup = "basic"
    if "document_text" not in st.session_state:
        st.session_state.document_text = ""
    if "documents" not in st.session_state:
        st.session_state.documents = {}
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = config["default_model"]
    
    # Header
    st.markdown("<h1 class='main-header'>LLM Evolution Explorer</h1>", unsafe_allow_html=True)
    st.markdown("An interactive app to explore the evolution of LLMs — from basic queries to agentic RAG integrations.")
    
    # Sidebar for setup selection and API key
    with st.sidebar:
        st.markdown("<h2 class='sub-header'>Setup</h2>", unsafe_allow_html=True)
        
        # API Key input
        if not st.session_state.api_key_submitted:
            st.markdown("<div class='info-box'>Please enter your Gemini API key to continue.</div>", unsafe_allow_html=True)
            api_key = st.text_input("Gemini API Key", type="password")
            if st.button("Submit API Key"):
                if api_key:
                    save_api_key(api_key)
                    if initialize_gemini():
                        st.session_state.api_key_submitted = True
                        st.success("API key submitted successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to initialize Gemini API. Please check your API key.")
                else:
                    st.error("Please enter an API key.")
        
        # Setup selection
        if st.session_state.api_key_submitted:
            st.markdown("<h3>Select LLM Setup</h3>", unsafe_allow_html=True)
            setup_options = {
                "basic": "Basic LLM Query",
                "rag": "RAG Integration",
                "agentic": "Simple Agentic Tool Use",
                "agentic_rag": "Agentic RAG Integration"
            }
            
            setup_descriptions = {
                "basic": "Simple query-response interaction with the LLM.",
                "rag": "Retrieval-Augmented Generation using document context.",
                "agentic": "LLM with tool-use capabilities for GitHub integration.",
                "agentic_rag": "Advanced integration combining agentic capabilities with RAG."
            }
            
            selected_setup = st.radio(
                "Choose a setup:",
                options=list(setup_options.keys()),
                format_func=lambda x: setup_options[x],
                index=list(setup_options.keys()).index(st.session_state.current_setup)
            )
            
            if selected_setup != st.session_state.current_setup:
                st.session_state.current_setup = selected_setup
                st.rerun()
            
            st.markdown(f"<div class='info-box'>{setup_descriptions[selected_setup]}</div>", unsafe_allow_html=True)
            
            # Add model selector
            st.session_state.selected_model = add_model_selector()
    
    # Main content based on selected setup
    if not st.session_state.api_key_submitted:
        st.info("Please enter your Gemini API key in the sidebar to continue.")
        return
    
    # Display conceptual architecture
    st.markdown("<h2 class='sub-header'>Conceptual Architecture</h2>", unsafe_allow_html=True)
    display_architecture(st.session_state.current_setup)
    
    # Display dynamic macro overview
    st.markdown("<h2 class='sub-header'>Workflow Overview</h2>", unsafe_allow_html=True)
    display_workflow(st.session_state.current_setup)
    
    # Setup-specific content
    st.markdown("<h2 class='sub-header'>Interaction</h2>", unsafe_allow_html=True)
    
    if st.session_state.current_setup == "basic":
        basic_llm_query()
    elif st.session_state.current_setup == "rag":
        rag_integration()
    elif st.session_state.current_setup == "agentic":
        agentic_tool_use()
    elif st.session_state.current_setup == "agentic_rag":
        agentic_rag_integration()

def display_architecture(setup):
    """Display the conceptual architecture for the selected setup."""
    architectures = {
        "basic": """
        ```
        User Query → Gemini API → Response
        ```
        
        In this basic setup, user queries are sent directly to the Gemini API, which processes the input and returns a response based on its pre-trained knowledge.
        """,
        
        "rag": """
        ```
        Document → Text Extraction → Context Storage
                                        ↓
        User Query → Query Processing → Gemini API → Response
                                        ↑
                                    Context Retrieval
        ```
        
        In the RAG setup, documents are processed to extract text, which is stored as context. When a user submits a query, relevant context is retrieved and combined with the query before being sent to the Gemini API, enhancing the response with document-specific information.
        """,
        
        "agentic": """
        ```
        User Query → Query Analysis → Gemini API ⟷ Tool Selection → GitHub Tool → GitHub API
                                        ↓
                                     Response
        ```
        
        In the agentic setup, the LLM analyzes the user query and determines if it needs to use tools to fulfill the request. It can interact with the GitHub tool to retrieve repository information, which is then incorporated into the response.
        """,
        
        "agentic_rag": """
        ```
        Documents → Text Extraction → Context Storage
                                        ↓
        User Query → Query Analysis → Gemini API ⟷ Tool Selection → GitHub Tool → GitHub API
                                        ↑               ↓
                                    Context Retrieval   Other Tools
                                        ↓
                                     Response
        ```
        
        The agentic RAG setup combines both approaches. The LLM has access to document context through RAG and can also use tools like the GitHub integration. It intelligently decides which sources and tools to use based on the query, providing comprehensive responses with citations.
        """
    }
    
    st.markdown(f"<div class='card'>{architectures[setup]}</div>", unsafe_allow_html=True)

def display_workflow(setup):
    """Display the dynamic workflow overview for the selected setup."""
    workflows = {
        "basic": [
            "User submits a query",
            "Query is sent to Gemini API",
            "Gemini processes the query using its pre-trained knowledge",
            "Response is returned to the user"
        ],
        
        "rag": [
            "User uploads a document",
            "Document text is extracted and processed",
            "User submits a query related to the document",
            "Query and relevant document context are sent to Gemini API",
            "Gemini generates a response incorporating document information",
            "Response with citations is returned to the user"
        ],
        
        "agentic": [
            "User submits a query related to GitHub repositories",
            "Query is analyzed to determine if tool use is needed",
            "If needed, the GitHub tool is called to retrieve repository information",
            "Information from the tool is incorporated into the context",
            "Gemini generates a response using the enhanced context",
            "Response is returned to the user"
        ],
        
        "agentic_rag": [
            "User uploads multiple documents",
            "Document texts are extracted and processed",
            "User submits a query",
            "Query is analyzed to determine needed context and tools",
            "Relevant document context is retrieved",
            "If needed, tools like GitHub integration are called",
            "All information is combined into an enhanced context",
            "Gemini generates a comprehensive response with citations",
            "Response is returned to the user"
        ]
    }
    
    for i, step in enumerate(workflows[setup]):
        st.markdown(f"**Step {i+1}:** {step}")

def basic_llm_query():
    """Implement the basic LLM query functionality."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("Enter your query below to get a response from Gemini.")
    
    query = st.text_area("Your query:", height=100)
    
    if st.button("Submit Query"):
        if query:
            with st.spinner("Generating response..."):
                response = generate_response(query, st.session_state.selected_model)
                st.markdown("### Response:")
                st.markdown(response)
        else:
            st.warning("Please enter a query.")
    
    st.markdown("</div>", unsafe_allow_html=True)

def rag_integration():
    """Implement the RAG integration functionality."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Document upload
    st.markdown("### Upload Document")
    uploaded_file = st.file_uploader("Upload a PDF document:", type=["pdf"])
    
    if uploaded_file:
        if "document_path" not in st.session_state or st.session_state.document_path != uploaded_file.name:
            with st.spinner("Processing document..."):
                # Save the uploaded file
                file_path = save_uploaded_file(uploaded_file, config["temp_folder"])
                
                # Extract text from the PDF
                document_text = extract_text_from_pdf(file_path)
                
                # Store in session state
                st.session_state.document_text = document_text
                st.session_state.document_path = uploaded_file.name
                
                st.success(f"Document '{uploaded_file.name}' processed successfully!")
    
    # Query input
    st.markdown("### Ask a Question About the Document")
    
    if st.session_state.document_text:
        query = st.text_area("Your question:", height=100)
        
        if st.button("Submit Question"):
            if query:
                with st.spinner("Generating response..."):
                    response = generate_rag_response(query, st.session_state.document_text, st.session_state.selected_model)
                    st.markdown("### Response:")
                    st.markdown(response)
            else:
                st.warning("Please enter a question.")
    else:
        st.info("Please upload a document first.")
    
    st.markdown("</div>", unsafe_allow_html=True)

def agentic_tool_use():
    """Implement the agentic tool use functionality."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### GitHub Repository Query")
    
    # Import the GitHub tool here to avoid circular imports
    from utils.github_tool import GitHubTool
    
    # Default repository from config
    default_repo = config['github_repo']
    
    # Option to use custom repository
    use_custom_repo = st.checkbox("Use custom repository URL", value=False)
    
    if use_custom_repo:
        repo_url = st.text_input("GitHub Repository URL:", 
                                placeholder="https://github.com/username/repository",
                                value=default_repo)
        st.markdown("Ask questions about the specified GitHub repository.")
    else:
        repo_url = default_repo
        st.markdown(f"Ask questions about the Model Context Protocol Python SDK repository: {repo_url}")
    
    query = st.text_area("Your query about the repository:", height=100, 
                         placeholder="Example: What are the recent issues in the repository?")
    
    if st.button("Submit Repository Query"):
        if query:
            with st.spinner("Processing query..."):
                # First, generate a response using Gemini
                response = generate_response(f"The user is asking about the GitHub repository: {repo_url}. The query is: {query}", st.session_state.selected_model)
                
                # Initialize GitHub tool
                github_tool = GitHubTool()
                github_tool.repo_url = repo_url  # Update the repository URL
                
                # Extract owner and repo name from URL
                parts = repo_url.split('/')
                if len(parts) >= 5:
                    repo_owner = parts[-2]
                    repo_name = parts[-1]
                    
                    # Display repository info
                    st.markdown(f"### Repository: {repo_owner}/{repo_name}")
                    
                    # Display response
                    st.markdown("### Response:")
                    st.markdown(response)
                    
                    # Show repository issues
                    st.markdown("### Repository Issues:")
                    
                    # Use asyncio to run the async method
                    async def get_issues():
                        return await github_tool.list_repository_issues(repo_owner, repo_name)
                    
                    issues = asyncio.run(get_issues())
                    if isinstance(issues, list):
                        for issue in issues:
                            st.markdown(f"**#{issue['number']}**: {issue['title']} ({issue['state']})")
                            st.markdown(f"Created: {issue['created_at']}")
                            st.markdown(f"Description: {issue['body']}")
                            st.markdown("---")
                    else:
                        st.warning(f"Could not fetch issues: {issues}")
                    
                    # Show available tools (for demonstration)
                    st.markdown("### Available Tools:")
                    st.info("This would normally be handled automatically by the agentic LLM, but for demonstration purposes, we're showing the available tools here.")
                    
                    # Use asyncio to run the async method
                    async def run_async():
                        tools = await github_tool.discover_available_tools()
                        return tools
                    
                    tools = asyncio.run(run_async())
                    st.json(tools)
                else:
                    st.error("Invalid repository URL format. Please use the format: https://github.com/username/repository")
        else:
            st.warning("Please enter a query.")
    
    st.markdown("</div>", unsafe_allow_html=True)

def agentic_rag_integration():
    """Implement the agentic RAG integration functionality."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Document upload
    st.markdown("### Upload Documents")
    uploaded_file = st.file_uploader("Upload a PDF document:", type=["pdf"], key="agentic_rag_uploader")
    
    if uploaded_file:
        if uploaded_file.name not in st.session_state.documents:
            with st.spinner("Processing document..."):
                # Save the uploaded file
                file_path = save_uploaded_file(uploaded_file, config["temp_folder"])
                
                # Extract text from the PDF
                document_text = extract_text_from_pdf(file_path)
                
                # Store in session state
                st.session_state.documents[uploaded_file.name] = {
                    "path": file_path,
                    "text": document_text
                }
                
                st.success(f"Document '{uploaded_file.name}' processed successfully!")
    
    # Display uploaded documents
    if st.session_state.documents:
        st.markdown("### Uploaded Documents:")
        for doc_name in st.session_state.documents:
            st.markdown(f"- {doc_name}")
    
    # Query input
    st.markdown("### Ask a Question")
    st.markdown("Your question can reference the uploaded documents and/or the GitHub repository.")
    
    query = st.text_area("Your question:", height=100, key="agentic_rag_query")
    
    if st.button("Submit Question", key="agentic_rag_submit"):
        if query:
            with st.spinner("Generating response..."):
                # Combine all document texts
                all_docs_text = ""
                for doc_name, doc_info in st.session_state.documents.items():
                    all_docs_text += f"\n\n--- Document: {doc_name} ---\n{doc_info['text']}"
                
                # Generate response with RAG
                if all_docs_text:
                    response = generate_rag_response(
                        f"The user is asking about the GitHub repository: {config['github_repo']} and possibly the uploaded documents. The query is: {query}",
                        all_docs_text,
                        st.session_state.selected_model
                    )
                else:
                    response = generate_response(
                        f"The user is asking about the GitHub repository: {config['github_repo']}. The query is: {query}",
                        st.session_state.selected_model
                    )
                
                st.markdown("### Response:")
                st.markdown(response)
                
                # Show GitHub integration (for demonstration)
                st.markdown("### GitHub Integration:")
                st.info("This would normally be handled automatically by the agentic LLM, but for demonstration purposes, we're showing the GitHub integration here.")
                
                # Import the GitHub tool here to avoid circular imports
                from utils.github_tool import GitHubTool
                
                # Initialize GitHub tool
                github_tool = GitHubTool()
                
                # Use asyncio to run the async method
                async def run_async():
                    issues = await github_tool.list_repository_issues()
                    return issues
                
                issues = asyncio.run(run_async())
                st.json(issues)
        else:
            st.warning("Please enter a question.")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
