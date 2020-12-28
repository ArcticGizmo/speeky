import os
import deepspeech
import wave
import numpy as np

DIRNAME = os.path.dirname(__file__)

PBMM_PATH = os.path.join(DIRNAME, 'models/deepspeech-0.9.3-models.pbmm')
SCORER_PATH = os.path.join(DIRNAME, 'models/deepspeech-0.9.3-models.scorer')

LM_ALPHA = 0.75
LM_BETA = 1.85
BEAM_WIDTH = 500

def create_model():
  model = deepspeech.Model(PBMM_PATH)
  model.enableExternalScorer(SCORER_PATH)

  # set the hyperparamters for better accuracy
  model.setScorerAlphaBeta(LM_ALPHA, LM_BETA)

  # set the beam width (higher is more accurate but slower)
  model.setBeamWidth(BEAM_WIDTH)

  return model

def decode_file(model, path):
  wav = wave.open(path, 'r')
  frames = wav.getnframes()
  buffer = wav.readframes(frames)
  data16 = np.frombuffer(buffer, dtype=np.int16)

  return model.stt(data16)
