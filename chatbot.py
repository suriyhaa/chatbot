import spacy

nlp = spacy.load("en_core_web_sm")

# Sample corpus
corpus = """Hello! I'm your chatbot. I can help you with basic questions. 
How can I assist you today? Ask me anything about weather, time, or general knowledge."""

# Convert to spaCy doc
doc = nlp(corpus)

# Get sentences
sent_tokens = [sent.text for sent in doc.sents]

# Very basic response logic
def get_response(user_input):
    user_doc = nlp(user_input.lower())
    for sent in sent_tokens:
        if user_doc.similarity(nlp(sent)) > 0.7:
            return sent
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Chat loop
print("Chatbot: Hi! Ask me anything.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'bye', 'quit']:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", get_response(user_input))
