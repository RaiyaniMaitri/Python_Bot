from flask import Flask, render_template, request, jsonify
import random
import nltk

nltk.download('punkt')

app = Flask(__name__)

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    },
    "how_are_you": {
        "patterns": ["how are you", "how's it going", "how do you feel"],
        "responses": ["I'm just a program, but thanks for asking!", "Doing great! How about you?"]
    },
    "help": {
        "patterns": ["help", "assist", "i need help", "can you help me"],
        "responses": ["Of course! What do you need help with?", "I'm here to assist you. Please provide more details."]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "farewell"],
        "responses": ["Goodbye! Have a great day!", "See you later! Take care!"]
    },
    "default": {
        "patterns": [],
        "responses": ["I'm not sure how to respond to that. Could you elaborate?", "That sounds interesting! Tell me more."]
    }
}

def detect_intent(message):
    message = message.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in message:
                return intent
    return "default"

def chatbot_response(message):
    intent = detect_intent(message)
    return random.choice(intents[intent]["responses"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User message: {user_message}")  
    
    response = chatbot_response(user_message)
    print(f"Chatbot response: {response}") 
    
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
