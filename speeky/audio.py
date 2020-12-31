import speech_recognition as sr
import pyttsx3 as tts

ttsEngine = tts.init()

def say(text):
    ttsEngine.say(text)
    ttsEngine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(source)
        print('--- listening')
        audio = r.listen(source)
        print(audio)
        said = ""

        try:
            said = r.recognize_sphinx(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
