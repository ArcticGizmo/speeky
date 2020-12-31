import os
from speeky import stt, regy, action
import speech_recognition as sr
import pyttsx3 as tts
import json

DIRNAME = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(DIRNAME, '..', 'actions.json')

ttsEngine = tts.init()


def speak(text):
    ttsEngine.say(text)
    ttsEngine.runAndWait()


def getAudio():
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


def getConfig(path):
    with open(path) as file:
        data = json.load(file)
    return data


def _main():
    config = getConfig(CONFIG_PATH)
    actions = [action.fromConfig(a) for a in config["actions"]]

    print("Welcome to speeky, a text to action converter")
    print("Options:")
    print("* exit - will exit the loop")
    print("* list - will list all available actions")
    print("\n")
    print("Begin typing to see what it can do")

    while True:
        text = input("|> ").lower()
        if (text == 'exit'):
            return

        if (text == 'list'):
            [print('* {}'.format(a)) for a in actions]


if __name__ == "__main__":
    _main()
