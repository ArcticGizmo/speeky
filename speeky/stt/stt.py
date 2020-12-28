import os
import deepspeech as ds

from pathlib import Path

PBMM_PATH = Path('../models/deepspeech-0.93-modals.pbmm')
SCORER_PATH = Path('../models/deepspeech-0.93-modals.scorer')

LM_ALPHA = 0.75
LM_BETA = 1.85
BEAM_WIDTH = 500

def create_model():
  model = ds.Model(PBMM_PATH)
  model.enableExternalScorer(SCORER_PATH)

  # set the hyperparamters for better accuracy
  model.setScorerAlphaBeta(LM_ALPHA, LM_BETA)

  # set the beam width (higher is more accurate but slower)
  model.setBeamWidth(BEAM_WIDTH)

