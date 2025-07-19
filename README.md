# AutoGen Simple Chat Demo

A simple multi-agent chat application built with Microsoft AutoGen.

## Features

- Multi-agent conversation system
- UserProxy agent for human interaction
- Assistant agent for AI responses
- Group chat management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/mukemitt/autogen_demo1.git
cd autogen_demo1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. Run the application:
```bash
python simple_chat.py
```

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection

## Usage

The application creates a simple chat interface where you can interact with an AI assistant through the AutoGen framework. The conversation will continue until you type 'exit' or the maximum rounds are reached.