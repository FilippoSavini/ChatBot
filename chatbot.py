import numpy as np
import speech_recognition as sr
from gtts import gTTS
import transformers
import time
import datetime
import os

# Build the model
class ChatBot():
    def __init__(self, name):
        print("--engine on--", name, "is ready to serve you")
        self.name = name
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("I am listening...")
            audio = recognizer.listen(mic) 
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me --> ERROR")
    @staticmethod
    def text_to_speech(text):
        print("Jarvis --> ", text)
        tts = gTTS(text = text, lang = "en", slow = False)
        filename = "voice.mp3"
        tts.save(filename)
        statbuf = os.stat(filename)
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        os.system("start voice.mp3")
        time.sleep(int(duration*50))
        os.remove(filename)
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime("%H:%M")
    
# running the model    
if __name__ == "__main__":
    ai = ChatBot(name = "Jarvis")
   
    nlp = transformers.pipeline("conversational", model = "microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex = True
    while ex:
        ai.speech_to_text()
        # wake up
        if ai.wake_up(ai.text):
            res = "Hi, I am Jarvis, your personal assistant, how can I help you?"
            # ai.text_to_speech("How can I help you?")
            # ai.speech_to_text()
        # action time
        elif "time" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["thanks", "thank you"]):
            res =  np.random.choice(["you're welcome", "no problem", "my pleasure"])
        elif any(i in ai.text for i in ["bye", "goodbye", "exit", "close"]):
            res = np.random.choice(["bye", "goodbye", "see you later"])
            ex = False
        else:
            if ai.text == "ERROR":
                res = "I can't understand you"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id = 50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6: ].strip()
        ai.text_to_speech(res)
    print("--engine off--")
        