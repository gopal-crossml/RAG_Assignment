# AI Agent Project (LangChain + Google Gemini)

This repository showcases how to build an AI-driven agent using LangChain with Google Gemini (Generative AI) as the language model. The project focuses on clean structure, secure credential handling, and optional PDF-based output generation.

It’s intended to be a lightweight yet extensible foundation for creating RAG pipelines, AI agents, and document-centric AI workflows.

## 🚀 Key Features

🔗 LangChain-powered workflows for agent orchestration

🤖 Google Gemini (Generative AI) as the LLM backend

📄 PDF generation support for saving AI outputs

🧩 Modular architecture for prompts, credentials, and constants

## 🧰 Prerequisites

-Python 3.10 or 3.11 (3.14+ supported but optional)

-Google Generative AI (Gemini) API key

-Virtual environment (recommended)

## 📦 Setup & Installation

1️⃣ Clone the Repository
  ```bash
  git clone https://github.com/gopal-crossml/RAG_Assignment.git
  cd project RAG_Assignment
  ```
2️⃣ Create and Activate a Virtual Environment 
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
3️⃣ Install Dependencies
  ```bash
  pip install -r requirement.txt
  ```
## 🔐 Environment Configuration

Create a .env file:
  ```bash
  GOOGLE_API_KEY=your_google_genai_api_key
  ```
⚠️ Ensure .env is included in .gitignore to prevent accidental exposure of secrets.

## ▶️ Running the Application

Start the project by running:
  ```bash
  python main.py
  ```

Based on your setup, the agent will:

-Load prompt templates from prompt.py

-Authenticate using logic in cred.py

-Read shared configuration from constant.py

-Generate AI-powered responses

-Optionally write outputs to a PDF file (temp.pdf)

## 🛠️ Customization Guide
**✍️ Prompts**

  Modify prompt.py to update system messages, user instructions, or task-specific prompts.

## ⚙️ Constants

Use constant.py to manage reusable configuration values such as:

-Model names

-Temperature settings

-File paths

## 🔑 Credentials

Handle API keys and sensitive logic inside cred.py to keep concerns separated and secure.

## 📄 Sample Output

The agent can produce structured AI responses and store them in a PDF file:

temp.pdf


You can customize or disable PDF creation logic inside main.py.

## 🧪 Development Notes

-Use print() statements or logging for debugging agent outputs

-Keep prompts modular and version-controlled

-Never commit .env files or API keys

## 🤝 Contributions

Contributions are encouraged and appreciated!

-Fork the repository

-Create a new feature branch

-Commit your changes

-Open a Pull Request