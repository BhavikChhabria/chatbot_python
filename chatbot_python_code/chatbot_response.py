import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

#Download Necessary Package 

nltk.download('punkt')
nltk.download('wordnet')

#Loads intents data from Json file as given name as intents.json

with open('intents.json', 'r') as file:
    data = json.load(file)

#Initialize with structure  
lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []


for intent in data['intents']:
    for pattern in intent['patterns']:
      
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        
        
        documents.append((word_list, intent['tag']))
        

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize, lower and sort words and classes logic define below
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ['?', '!']]
words = sorted(set(words))
classes = sorted(classes)

def clean_sentence(sentence):
    """Tokenizes and lemmatizes a sentence."""
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def predict_intent_tag(sentence):
    """Predicts the intent tag based on a sentence."""
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in sentence.lower():
                return intent['tag']
    return "unknown"

def get_response(tag):
    """Gets a random response based on the intent tag."""
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."

def chatbot_response(sentence):
    """Generates a chatbot response based on the user's sentence."""
    tag = predict_intent_tag(sentence)
    return get_response(tag)

print("Hello! I'm here to help. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
