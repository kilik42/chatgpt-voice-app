import openai 
import pyttsx3 # Text to speech
import speech_recognition as sr # for speech recognition
import datetime # for date and time
# import wikipedia # for wikipedia
# import webbrowser # for opening browser
# import os # for operating system
# import smtplib # for sending email
# import random # for random number
# import pywhatkit # for playing youtube
# import pyjokes # for jokes
# import requests # for getting weather

# API key
openai.api_key = " "

# Text to speech
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def generate_response(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=0.9,
        max_tokens=4000,
        n=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=None,
       
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Listening...")
        print(" say 'genius' to start recording your question...")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                transcription = r.recognize_google(audio, language='en-in')
                #record audio if transcription.lower() == "genius":
                if transcription.lower() == "genius":
                    recognizer = sr.Recognizer()
                    source.pause_threshold = 1
                    audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                #transcribe audio to text
                text = transcribe_audio_to_text(filename)
                if text:
                    print(f"you said: {text}")
                    #generate response
                    response = generate_response(text)
                    print(f"genius said: {response}")
                    #read response using text to speech
                    speak_text(response)
            except Exception as e:
                print(e)
                print("Say that again please...")
                print("an error occurred {}".format(e))
                return "None"


if __name__ == '__main__':
    main()