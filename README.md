#AI Chatbot with spaCy

This is a basic AI chatbot built using the `spaCy` NLP library in Python. It can respond to simple user queries based on text similarity.

##Features

- Built with `spaCy` and `en_core_web_sm`
- Basic response logic using semantic similarity
- Command-line chat interface
- Easily extendable with more intents or answers

##Requirements

- Python 3.7+
- spaCy

## Installation

1. Clone this repo:

```bash
git clone https://github.com/suriyhaa/chatbot.git
cd chatbot

2. Create and activate a virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate

3.Install dependencies:

pip install spacy
python -m spacy download en_core_web_sm


4.Run the chatbot from your terminal:

python chatbot.py
Type your messages and the bot will respond. Type exit, bye, or quit to end the session.

5.Example

You: How can you help me?
Chatbot: How can I assist you today?
