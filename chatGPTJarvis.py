# Python virtual assistant program 
# to generate text to speech with ChatGPT

import speech_recognition as sr
import pyttsx3

import os
OPENAI_KEY = "YOUR_OPEN_AI_KEY"

# If not connecting, might need to be signed
# into OpenAI

import openai
openai.api_key = OPENAI_KEY

# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
# Loop in case of errors
    while True:
        try:
            # use the microphone as source of input
            with sr.Microphone() as source:

                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source=source, duration=0.2)

                print("I'm listening")

                # listens for the user's input
                audio = r.listen(source)

                # Using google to recognize audio
                MyText = r.recognize_google(audio)
                print(MyText)

                return MyText

        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")

# Newer model might work better
def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = []
while True:
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)

    print(response)