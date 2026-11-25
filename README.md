# AI Agent with Tool Calling

## Project Overview

This project is an AI Agent built using Python, LangChain, and Google's Gemini AI model.

The agent understands user requests and automatically selects the appropriate tool to perform tasks.

It includes two tools:
- **Calculator Tool:** Performs mathematical calculations.
- **File Lookup Tool:** Searches for information in a text file.

## Technologies Used

- Python
- LangChain
- Google Gemini AI
- LangChain Google GenAI
- Python Dotenv

## Project Architecture

```text
AI Agent with Tool Calling/
│
├── agent/
│   └── main_agent.py
│
├── tools/
│   ├── calculator.py
│   └── file_lookup.py
│
├── examples/
│   └── sample_executions.txt
│
├── sample_data.txt
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Features

1. AI-powered tool selection based on user requests.
2. Mathematical calculations using the Calculator Tool.
3. Text searching using the File Lookup Tool.
4. Gemini AI integration through LangChain.
5. Error handling for unexpected failures.
6. Interactive command-line interface.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the Project Folder

```bash
cd "AI Agent with Tool Calling"
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install langchain langchain-google-genai python-dotenv
```

### 6. Configure API Key

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not share or upload your API key publicly.

## How to Run

Execute the following command:

```bash
python main.py
```

Enter your questions in the terminal.

Type `exit` to stop the agent.

## Sample Executions

### Test 1: Calculator Tool

**User Input:**

Calculate 125 multiplied by 8 using the calculator tool.

**Tool Selected:** calculator

**Output:** 1000

**Result:** Successful

### Test 2: File Lookup Tool

**User Input:**

Search the sample_data.txt file for LangChain.

**Tool Selected:** file_lookup

**Output:**

LangChain is a framework for building applications using language models.

**Result:** Successful

## Error Handling

The project includes error handling for:
- Invalid mathematical expressions.
- Missing sample data files.
- File search failures.
- API and agent execution errors.

## Design Decisions

- LangChain is used to build the AI agent and manage tool calling.
- Google Gemini is used as the language model.
- Separate Python modules are used for individual tools.
- The agent selects tools according to the user's request.
- Environment variables are used to protect API credentials.

## Author

Gouri Chinchkar

