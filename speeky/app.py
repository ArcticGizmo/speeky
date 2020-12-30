import os
from speeky import stt, regy
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import playsound
import pyttsx3 as tts

ttsEngine = tts.init()

DIRNAME = os.path.dirname(__file__)

SAMPLE_1 = os.path.join(DIRNAME, 'sample_audio/1.wav')
SAMPLE_2 = os.path.join(DIRNAME, 'sample_audio/2.wav')
SAMPLE_3 = os.path.join(DIRNAME, 'sample_audio/3.wav')


def speak(text):
    ttsEngine.say(text)
    ttsEngine.runAndWait()


def get_audio():
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
def _main():
    print("--- main")
    model = stt.create_model()
    print(stt.decode_file(model, SAMPLE_1))


def _main2():
    text = input("Type something to say:")
    speak(text)
    print("Now listening")
    text = get_audio()

def _main3():
    regy.main()


if __name__ == "__main__":
    # _main()
    # _main2()
    _main3()
