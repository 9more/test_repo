# AI Assistant

## Status

In Development

---

## Overview

The AI Assistant is a full-stack conversational application designed to demonstrate modern AI application development. The project combines a React frontend with a Flask backend and integrates Google's Gemini large language model (LLM) to provide intelligent, real-time responses through a web interface.

Unlike a traditional chatbot, the application is being developed as an extensible AI platform capable of understanding my professional portfolio, answering questions about my projects and experience, and supporting future AI capabilities such as Retrieval-Augmented Generation (RAG), tool calling and cloud deployment.

---

## Objective

The primary objective of this project is to gain practical experience in designing, developing and deploying production-style AI applications while applying software engineering best practices.

The project serves as a central portfolio application that demonstrates my ability to integrate frontend development, backend APIs, prompt engineering, LLMs and machine learning into a single application.

---

## Technologies

### Frontend

- React
- TypeScript
- Vite
- HTML
- CSS

### Backend

- Python
- Flask
- Flask-CORS

### AI

- Google Gemini API
- Prompt Engineering

### Development

- Git
- GitHub
- REST APIs

---

## Key Features

### Current Features

- Conversational chat interface
- Real-time streaming AI responses
- Conversation memory
- Modular backend architecture
- Prompt engineering
- Error handling
- Responsive user interface

### Planned Features

- Portfolio knowledge base
- Retrieval-Augmented Generation (RAG)
- Tool calling
- Conversation persistence
- Docker deployment
- AWS cloud deployment
- CI/CD pipeline
- Authentication
- Analytics and monitoring

---

## Technical Implementation

The frontend is built using React and communicates with a Flask backend through REST API endpoints.

User messages are submitted to the backend where they are processed by the Gemini API. Responses are streamed back to the browser, allowing users to see the AI generate answers in real time rather than waiting for the complete response.

The backend has been structured into separate modules responsible for prompt management, conversation memory, routing and model communication to improve maintainability and support future expansion.

The application is currently being extended with a local knowledge base that will allow the assistant to answer questions about my portfolio using project documentation rather than relying solely on the LLM's general knowledge.

---

## Challenges & Solutions

### Streaming Responses

Implementing real-time streaming required coordinating communication between the React frontend, Flask backend and Gemini API. This was achieved using server-sent events (SSE) and incremental response rendering.

### Maintainability

To avoid placing all application logic inside a single file, the backend was divided into logical modules responsible for configuration, prompts, conversation memory and routing.

### Scalability

The architecture is intentionally modular so that future capabilities such as Retrieval-Augmented Generation, external tools and cloud deployment can be added without significant changes to the existing codebase.

---

## Skills Demonstrated

- Full-stack development
- AI application development
- Large Language Model integration
- Prompt engineering
- REST API development
- Flask
- React
- TypeScript
- Python
- Software architecture
- Streaming responses
- Conversation management
- Git version control

---

## Future Enhancements

Planned enhancements include:

- Retrieval-Augmented Generation (RAG)
- Semantic search
- Portfolio document retrieval
- Tool integration
- AWS deployment
- Docker containerisation
- CI/CD automation
- User authentication
- Conversation persistence
- Performance monitoring
