# ChatBot

## Description
This code implements a simple chatbot named "Jarvis". The chatbot is capable of listening to audio through a microphone, converting it into text, and responding vocally using the text-to-speech engine. The chatbot can also perform some actions such as providing the current time, responding to thanks and greetings, and engaging in general conversation.

## Dependencies
The code relies on the following Python libraries:
- `numpy` for mathematical operations
- `speech_recognition` for speech recognition
- `gtts` for text-to-speech
- `transformers` for using language models

You can install the dependencies via `pip` by running the following command:

## Usage
To run the chatbot, simply execute the provided Python script (`chatbot.py`). When the chatbot is running, follow the provided voice instructions to interact with it. The chatbot will respond to requests, provide the current time, handle thanks and greetings, and engage in generic conversations.

You can end the execution of the chatbot by typing "bye", "goodbye", "exit", or "close" during the interaction.

## Interaction Examples
Here are some examples of interaction with the chatbot:

- User: "Hey Jarvis, what time is it?"
  - ChatBot: "It's 2:30 PM."
  
- User: "Thanks for the help!"
  - ChatBot: "You're welcome, I'm here to assist you."

- User: "Hi Jarvis, how are you?"
  - ChatBot: "Hello! I'm fine, thanks for asking."

## Note
It's important to note that this code utilizes online services for speech recognition and text-to-speech. Make sure you have an active internet connection while running the chatbot.
