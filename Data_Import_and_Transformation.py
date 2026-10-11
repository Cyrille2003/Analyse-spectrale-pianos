import pandas as pd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

Pianos = ["Erard1", "Pleyel1", "Steinway1"]
datas_for_pianos = {}       # Initialisation du dictionnaire des données, classées par piano.

for piano in Pianos :
    x, fs = sf.read(f"{piano}.wav", dtype="float64")
    if x.ndim > 1:
        x = x[:, 0]
    
    duration = sf.info(f"{piano}.wav").duration
    DT = 1/fs
    datas_for_pianos[piano] = [np.array(x), DT, duration]







