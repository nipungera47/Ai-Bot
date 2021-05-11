import pyttsx3 
import datetime
import speechRecognition as sr

 

engine = pyttsx3.init('sapi5')   # Api of microsoft used for voice
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)





def speak(audio):
    # pass
    engine.say(audio)
    engine.runAndWait()


def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning Dear")

    elif hour>=12 and hour<=18:
        speak("Good After Noon Dear")

    else:

        speak("Good Evening Dear")


    speak("I am here sir, How can i help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening ..... ")
        r.pause_threshold =1
        audio = r.listen(source)

try:
    print("Recognizing")
    # query = r.recognize


if __name__ == "__main__":
    Wish()

