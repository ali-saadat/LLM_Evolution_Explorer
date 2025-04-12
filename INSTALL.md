# LLM Evolution Explorer - Installation Guide

## Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

## Installation Steps


1. **Navigate to the project directory**
   ```
   cd llm_evolution_explorer
   ```

2. **Create a virtual environment** (recommended)
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```
   streamlit run app.py
   ```

6. **Access the application**
   - The application will automatically open in your default web browser
   - If it doesn't, you can access it at: http://localhost:8501

## Configuration

- When you first run the application, you'll be prompted to enter your Gemini API key
- You can obtain a Gemini API key from: https://ai.google.dev/
- The application will remember your API key for the duration of the session

## Features

- **Basic LLM Query**: Simple query-response interaction with Gemini
- **RAG Integration**: Upload PDF documents and ask document-specific questions
- **Simple Agentic Tool Use**: Query information about GitHub repositories
- **Agentic RAG Integration**: Combine document context with GitHub tool integration

## Troubleshooting

- If you encounter issues with the Gemini API, try selecting a different model from the dropdown
- If the application fails to start, ensure you have the correct Python version and all dependencies installed
- For any other issues, please refer to the README.md file or contact support

## Notes

- This application uses a mock implementation of the Model Context Protocol for GitHub integration
- All data is processed locally and no information is sent to external servers except for the Gemini API calls
