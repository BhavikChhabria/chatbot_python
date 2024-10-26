# Chatbot Creation

#### This project is a simple chatbot built with Python that uses intent classification to respond to user inputs. The chatbot identifies user intent based on pre-defined patterns in intents.json and provides responses accordingly.

## Features

Intent classification to understand user queries.
Customizable intents.json file for adding or modifying intents and responses.
Randomized responses from a set of predefined responses for each intent.

## Project Structure

#### -> intents.json: Contains various intents, each with patterns (phrases that trigger the intent) and responses (replies from the bot).

#### chatbot.py: Main code for the chatbot, which includes:

#### -> predict_intent_tag(sentence): A function that predicts the intent tag for a given user sentence.

#### -> get_response(tag): A function that returns a random response from the intents.json file based on the predicted intent tag.

#### -> chatbot_response(sentence): Combines intent prediction and response generation to provide a complete chatbot response.

## Project Analysis and Future Scope

This chatbot demonstrates a foundational approach to intent classification without machine learning.

#### Some future improvements could include:

#### (->)Machine Learning Integration: Adding NLP and ML techniques like word embeddings or TF-IDF to improve accuracy.

#### (->)Advanced Pattern Matching: Leveraging regex or NLP libraries like NLTK or spaCy to enhance pattern detection.

## Screenshots and Explaination

#### Python libraries such as json for data handling and random for response selection are fundamental to this project.

![alt text](<Screenshot (155).png>)

Jupyter Notebook Lab provides the testing environment for the chatbot, facilitating real-time testing and debugging.
The chatbot's primary function, chatbot_response, integrates both intent prediction and response generation.
Future expansions can include using machine learning or NLP libraries to enhance accuracy and allow more flexible, robust responses.

#### -> The objective of this project is to develop a simple, rule-based chatbot capable of recognizing user intent and generating relevant responses.

![alt text](<Screenshot (154)-1.png>)

#### -> The objective of this project is to develop a simple, rule-based chatbot capable of recognizing user intent and generating relevant responses.

![alt text](<Screenshot (149)-1.png>)

![alt text](<Screenshot (150)-1.png>)

#### -> The objective of this project is to develop a simple, rule-based chatbot capable of recognizing user intent and generating relevant responses.

![alt text](<Screenshot (151)-1.png>)

![alt text](<Screenshot (152)-1.png>)

#### -> The objective of this project is to develop a simple, rule-based chatbot capable of recognizing user intent and generating relevant responses.

![alt text](<Screenshot (153)-1.png>)

#### -> The objective of this project is to develop a simple, rule-based chatbot capable of recognizing user intent and generating relevant responses. The chatbot's functionality is based on Natural Language Processing (NLP) techniques, particularly focused on intent classification.

## Conclusion

This project offers an understanding of how a rule-based chatbot can be developed using Python and JSON data structures. By expanding the intents.json file and modifying the classification algorithm, one can customize and scale the chatbot’s capabilities. This project provides a foundation for exploring more advanced AI-driven chatbots in future studies.

### code and output

```python
import os
```

```python
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
```

```python
with open('intents.json', 'r') as file:
    data = json.load(file)
```

```python
words = []
classes = []
documents = []
```

```python
for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the sentence
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
```

```python
 documents.append((word_list, intent['tag']))
```

```python
 if intent['tag'] not in classes:
            classes.append(intent['tag'])
```

```python
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ['?', '!']]
words = sorted(list(set(words)))

```

```python
classes = sorted(classes)
```

```python
def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
```

```python
def predict_intent_tag(sentence):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in sentence.lower():
                return intent['tag']
    return "unknown"
```

```python
def get_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."

```

```python
def chatbot_response(sentence):
    tag = predict_intent_tag(sentence)
    return get_response(tag)
```

```python
chatbot_response("Hello")
```

    'Good to see you again!'

```python
chatbot_response("Is anyone there?")
```

    'Hi there, how can I help?'

```python
chatbot_response("Is anyone there?")
```

    'Good to see you again!'

```python
chatbot_response("Is anyone there?")
```

    'Hi there, how can I help?'

```python
chatbot_response("Is anyone there?")
```

    'Hello!'

```python
chatbot_response("cya")
```

    'Sad to see you go :('

```python
chatbot_response("name")
```

    'I am your helper'

```python
chatbot_response("okay")
```

    'I am glad I helped you'

```python
chatbot_response("okay")
```

    'I am glad I helped you'

```python
chatbot_response("okay")
```

    'I am glad I helped you'

```python
 chatbot_response("its ok")
```

    'Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.'

```python
chatbot_response("okk")
```

    'I am glad I helped you'

```python
chatbot_response("information about sports")
```

    'Our university encourages all-round development of students and hence provides sports facilities in the campus. For more details visit<a target="_blank" href=/"(LINK IF HAVE)">here</a>'

```python
chatbot_response( "fucker")
```

    'please use appropriate language'

```python
chatbot_response( "fucker")
```

    'Maintaining decency would be appreciated'

```python
chatbot_response("When is vacation")
```

    'Academic calender is given to you by your class-soordinators after you join your respective classes'

```python
chatbot_response("when will semester starts")
```

    'Here is the Academic Calendar  <a target="_blank" href="YOUR ACADEMIC CALENDER">website</a>'

```python
chatbot_response("You mother fucker")
```

    'please use appropriate language'

```python
chatbot_response("You mother fucker")
```

    'please use appropriate language'

```python
chatbot_response("(
```

    'Maintaining decency would be appreciated'

```python
chatbot_response("meaning of OP")
```

    "I'm not sure how to respond to that."

```python
chatbot_response("meaning of UNIVERSITY")
```

    'Our university offers Information Technology, computer Engineering, Mechanical engineering,Chemical engineering, Civil engineering and extc Engineering.'

```python
chatbot_response("what is 1 + 1")
```

    "I'm not sure how to respond to that."

```python
chatbot_response("what is the process of admission")
```

    'Application can also be submitted online through the Unversity\'s  <a target="_blank" href="LINK OF ADMISSION DOCUMENT">website</a>'

```python

```
