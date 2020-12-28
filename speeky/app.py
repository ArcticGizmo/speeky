import os
from speeky import stt


DIRNAME = os.path.dirname(__file__)

SAMPLE_1 = os.path.join(DIRNAME, 'sample_audio/1.wav')
SAMPLE_2 = os.path.join(DIRNAME, 'sample_audio/2.wav')
SAMPLE_3 = os.path.join(DIRNAME, 'sample_audio/3.wav')

def _main():
    print("--- main")
    model = stt.create_model()
    print(stt.decode_file(model, SAMPLE_1))



if __name__ == "__main__":
    _main()