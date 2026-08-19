# Recall

Recall is an AI-powered learning assistant designed to help users understand difficult content while they are reading online.

## Repository Structure

```text
recall/
├── backend/   # FastAPI, SQLAlchemy, Alembic, and Python dependencies
└── frontend/  # Vite, React, and TypeScript
```

## Local Development

### Backend

The backend reads its configuration from `backend/.env`.

```bash
cd backend
uv sync
uv run fastapi dev src/app/main.py
```

Run database migrations from the same directory:

```bash
uv run alembic upgrade head
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The goal of the project is to reduce the friction between encountering something confusing and actually understanding it. Instead of leaving a webpage, opening a separate AI tool, copying text, adding context, and manually organizing the response, Recall aims to make that learning workflow available directly alongside the content the user is reading.

## Project Aim

Recall allows a user to select text from a webpage and generate an explanation tailored to the level of detail they need.

A user should eventually be able to:

- Highlight text and request an AI-generated explanation.
- Choose between explanation styles such as beginner, concise, detailed, analogy, and code-focused.
- Use the surrounding webpage context so explanations are relevant to what the user is actually reading.
- Ask follow-up questions about a page.
- Save useful explanations as learning notes.
- Search and revisit previously learned concepts.
- Generate quizzes and study guides from webpage content.
- Receive grounded answers with references to relevant parts of the source page.

The long-term goal is to turn any webpage into an interactive learning environment.

## Core User Flow

The intended workflow is:

```text
Read a webpage
      ↓
Highlight something confusing
      ↓
Ask Recall to explain it
      ↓
Receive a context-aware explanation
      ↓
Ask follow-up questions
      ↓
Save useful information as notes
      ↓
Review notes, quizzes, and study guides later
```

## Chrome Extension Vision

Recall is being developed as a backend-first application with the goal of becoming a Chrome extension.

The Chrome extension will act as the primary frontend and communicate with the Recall API.

```text
Webpage
   ↓
Chrome Extension
   ↓
FastAPI Backend
   ↓
LLM Provider
   ↓
PostgreSQL / pgvector
```

The extension will eventually allow users to:

- Explain highlighted text without leaving the current webpage.
- Open explanations in a persistent side panel.
- Add the current webpage to Recall.
- Ask questions about the full page.
- Save explanations as notes.
- View previous learning history.
- Generate quizzes and study guides.

## Current Development Focus

The project is currently focused on building the backend foundation.

Current and near-term work includes:

- FastAPI API architecture.
- PostgreSQL persistence.
- User accounts and authentication.
- AI-generated explanations.
- Structured LLM responses.
- Multiple explanation modes.
- Explanation history.
- Learning notes.
- Page ingestion and semantic search.
- Retrieval-Augmented Generation (RAG).
- Chrome extension integration.

## Planned Architecture

```text
Chrome Extension
        ↓
     FastAPI
        ↓
 ┌──────┼───────────┐
 ↓      ↓           ↓
LLM  PostgreSQL   Redis
       + pgvector
                    ↓
                 Worker
```

### Backend

- FastAPI
- Pydantic
- Async SQLAlchemy
- PostgreSQL
- Alembic
- JWT authentication

### AI

- LLM-based explanation generation
- Structured outputs
- Prompt templates for different explanation modes
- Embeddings
- Retrieval-Augmented Generation
- Citation-grounded page question answering

### Future Infrastructure

- Redis
- Background workers
- Docker
- Automated testing and AI evaluation
- CI/CD

## Design Principles

Recall is being built around a few core principles:

### Context matters

An explanation should consider the selected text as well as the surrounding content and page metadata.

### Different users need different explanations

A beginner explanation should not look the same as a concise or detailed explanation.

### AI output should be structured

The backend uses validated response schemas instead of relying on arbitrary free-form model output.

### User data should be isolated

Explanations, notes, pages, and learning history belong to the authenticated user and should not be accessible by other users.

### AI should stay grounded

For page-level questions, Recall will retrieve relevant sections of the source page and provide answers based on that evidence rather than relying only on the model's general knowledge.

## Long-Term Vision

Recall is intended to evolve from a text-explanation tool into a personal learning layer for the web.

Over time, the application can build a history of the concepts a user has studied, identify recurring areas of difficulty, and adapt explanations based on the user's previous learning.

The broader vision is:

> **Turn any webpage into a personalized, interactive learning experience.**
