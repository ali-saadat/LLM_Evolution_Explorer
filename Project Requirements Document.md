# Updated Project Requirements Document

## 📌 Project Name
**LLM Evolution Explorer**  
An interactive app to explore the evolution of LLMs — from basic queries to agentic Retrieval-Augmented Generation (RAG) integrations.

## 🎯 Project Goal
To develop a Python Streamlit application that demonstrates the progression of Large Language Models (LLMs) — from simple query responses to advanced agentic RAG-based integrations, offering users a hands-on experience.

## 👥 Target Audience
- Developers
- AI enthusiasts
- Anyone interested in exploring LLM capabilities and their evolution

## 🛠️ Core Features

### 1. LLM Setup Selection
Let users select from different LLM setups:
- Basic LLM Query
- RAG Integration
- Simple Agentic Tool Use
- Agentic RAG Integration

Display clear descriptions for each setup.

### 2. Conceptual Architecture Display
Show a conceptual architecture diagram or textual description for the selected LLM setup.
Clearly explain the data flow, components, and tool interactions.

### 3. Dynamic Macro Overview
Present a dynamic, interactive overview of each setup's workflow.
Use UX principles to display step-by-step progress with real-time status indicators.

### 4. Basic LLM Query
Provide a text input field for users to submit queries.
Connect to Gemini via API and display its response.
Prompt user for their Gemini API key on app startup.

**Enhancement**: Added model selection dropdown to choose between available Gemini models.

### 5. RAG Integration
Allow users to upload a PDF document.
Extract document content for use in query augmentation.
Provide a text input for document-specific questions.
Use the extracted content to augment Gemini's responses and cite factual references from the document.

### 6. Simple Agentic Tool Use
Integrate with a mock GitHub tool implementation.
Let users input queries related to public GitHub repositories.
**Enhancement**: Added option to specify custom GitHub repository URLs.
Display enriched LLM-generated results including relevant repository information.

### 7. Agentic RAG Integration
Combine agentic capabilities with RAG.
Support uploading multiple documents.
Enable the LLM to intelligently use tools, retrieve information, and answer queries with multi-source citations.

### 8. GitHub Integration (Tool)
Implement a mock GitHub tool that simulates interaction with GitHub repositories.
Support:
- Listing issues from a repository
- Retrieving the content of a specific issue
- Discovering available tools

### 9. File Upload
Implement a clean, user-friendly file upload mechanism for RAG and Agentic RAG.
Support PDF file parsing.

### 10. Robust Error Handling
**Enhancement**: Implemented robust error handling for Gemini API integration.
**Enhancement**: Added model fallback mechanisms if the primary model fails.

## 🎨 UI / UX Design
- Modern, responsive, and intuitive design
- Streamlit native components for consistent look and feel
- Aesthetic guidelines:
  - Rounded corners, shadows
  - Consistent color palette
- Prioritize usability, feedback, and progress indicators

## 🖥️ Technology Stack
- Python 3.10+
- Streamlit
- Google Generative AI (Gemini API)
- PyPDF for document processing
- Mock implementation of Model Context Protocol for GitHub integration

## 📏 Development Guidelines
- Use Streamlit for frontend and backend integration
- Enforce robust error handling with clear error messages and user notifications
- Prompt user for Gemini API key on first use
- Store session state for persistent user experience

## 🎯 Quality Attributes
- Responsiveness across devices
- Accessibility
- Clean, performant, and maintainable code
- Robust error handling and fallback mechanisms

## 🤖 GenAI Implementation
- Integration with Gemini API for text generation
- Mock implementation of tool integrations allowing LLMs to interact with external services (like GitHub)
- Use LLM tools to manage context, citations, and decision-making

## 🚀 Future Enhancements
- Support for additional file types: DOCX, TXT
- Integration with other LLM services and AI models
- Expanded agentic tool integrations
- User authentication and authorization
- Data visualization and analytics dashboards
- Full implementation of Model Context Protocol

## 📊 Non-Functional Requirements
- Performance: Fast and responsive UI
- Scalability: Handle increasing user and request load
- Security: Protect user data, especially API keys and documents
- Maintainability: Well-structured, documented, and modular codebase
