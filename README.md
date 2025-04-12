# LLM Evolution Explorer

An interactive app to explore the evolution of LLMs — from basic queries to agentic Retrieval-Augmented Generation (RAG) integrations.

![LLM Evolution streamlit app screenshot](https://i.imgur.com/ivJyxez.jpeg)

## Overview

LLM Evolution Explorer demonstrates the progression of Large Language Models (LLMs) from simple query responses to advanced agentic RAG-based integrations, offering users a hands-on experience with different LLM setups.

## Features

### 1. LLM Setup Selection
- Basic LLM Query
- RAG Integration
- Simple Agentic Tool Use
- Agentic RAG Integration

### 2. Model Selection
- Choose between different available Gemini models
- Automatic fallback to alternative models if the primary one fails

### 3. Conceptual Architecture Display
Each setup includes a conceptual architecture diagram explaining the data flow, components, and tool interactions.

### 4. Dynamic Macro Overview
Interactive workflow visualization with step-by-step progress indicators.

### 5. Basic LLM Query
Submit queries directly to Gemini and view its responses.

### 6. RAG Integration
Upload PDF documents and ask document-specific questions with augmented responses.

### 7. Simple Agentic Tool Use
Query information about GitHub repositories using a mock implementation of the Model Context Protocol.
Specify custom GitHub repository URLs for more flexible exploration.

### 8. Agentic RAG Integration
Combine document context with GitHub tool integration for comprehensive responses.

### 9. GitHub Integration
Access GitHub repository information through a mock implementation that provides realistic sample data.

## Getting Started

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

### Prerequisites
- Python 3.10+
- Gemini API key

### Quick Start

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
streamlit run app.py
```

3. Enter your Gemini API key when prompted.

## Usage

1. Select an LLM setup from the sidebar.
2. Choose your preferred Gemini model from the dropdown.
3. View the conceptual architecture and workflow for the selected setup.
4. Interact with the setup:
   - Basic LLM Query: Enter a query and submit.
   - RAG Integration: Upload a PDF document, then ask questions about it.
   - Simple Agentic Tool Use: Specify a GitHub repository URL (or use the default) and ask questions about it.
   - Agentic RAG Integration: Upload documents and ask questions that may require both document context and GitHub information.

## Project Structure

```
llm_evolution_explorer/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── INSTALL.md              # Installation instructions
├── updated_requirements.md # Updated project requirements
├── utils/                  # Utility modules
│   ├── __init__.py         # Package initialization
│   ├── config.py           # Configuration utilities
│   ├── gemini_api.py       # Gemini API integration
│   ├── document_processor.py # PDF processing utilities
│   ├── github_tool.py      # Mock GitHub integration
│   └── model_selector.py   # Model selection utilities
```

## Technology Stack

- Python
- Streamlit
- Google Generative AI (Gemini)
- Mock implementation of Model Context Protocol
- PyPDF

## Future Enhancements

- Support for additional file types (DOCX, TXT)
- Integration with other LLM services
- Expanded agentic tool integrations
- User authentication
- Data visualization dashboards
- Full implementation of Model Context Protocol

## License

This project is licensed under the MIT License - see the LICENSE file for details.
