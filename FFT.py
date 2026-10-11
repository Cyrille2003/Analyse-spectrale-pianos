import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter
from Data_Import_and_Transformation import datas_for_pianos

DT = datas_for_pianos["Erard1"][1]
STEP = 400      # nombre d'indexs temporels skippés dans la boucle dans gen_data_for_3D.
K = 8000        # nombre de valeurs dans le vecteur sur lequel on veut rouler la FFT. On roule de la valeur a à la valeur a+k la FFT.

etiquettes = [55/2 * 2**i for i in range(-1, 10)]

def fft(data_vector:np.ndarray, a:int, dt:float) -> np.ndarray:
    """
    Parameters : 
    data_vector: le vecteur de données en amplitude selon le temps.
    a: indice de la première valeur sur laquelle on roule la FFT.
    k: 
    dt: incrément temporel des données.
    
    Return : 
    Spectre de fréquences
    """
    data_to_compute = data_vector[a:a+K]
    fenetre = np.hanning(K)
    X = sp.fft.rfft(data_to_compute * fenetre)
    amplitudes = 2 * np.abs(X) / np.sum(fenetre)

    # amplitudes = sp.fft.rfft(data_to_compute)
    frequencies = sp.fft.rfftfreq(K, d=dt)
    return frequencies, amplitudes

FREQ = None

def gen_data_for_3D(piano_name:np.ndarray) -> np.ndarray:
    data = datas_for_pianos[piano_name][0]
    SIZE_FOR_ITERATION = len(data) - K
    results = pd.DataFrame(columns=["Temps", "Amplitudes"])
    global FREQ
    freq, res_for_t1 = fft(data_vector=data, a=0, dt=DT)
    res_for_t1 = np.log10(res_for_t1)
    FREQ = np.log2(freq)
    results.loc[len(results)] = [0, res_for_t1]
    for t in np.arange(1, SIZE_FOR_ITERATION - K, STEP):
        _, amp = fft(data_vector=data, a=t, dt=DT)
        res_for_t = np.log10(amp)   # Échelle logarithmique pour les amplitudes également.
        results.loc[len(results)] = [t * DT, res_for_t]
        print(round(t / len(data) * 100, 2), "%")                   # Progression dans la génération des données.
    return results

def gen_plot_3D(piano:str) -> None:
    data_3D = gen_data_for_3D(piano_name=piano)
    time_vector = data_3D["Temps"]
    frequencies_vector = FREQ

    A = np.stack(data_3D["Amplitudes"].to_numpy())
    A = A.T                                         
    A = sp.ndimage.gaussian_filter(A, sigma=(1,1))
    T, F = np.meshgrid(time_vector, frequencies_vector)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    surface = ax.plot_surface(T, F, A, cmap="magma")
    ax.set_xlabel("$Temps [s]$")
    ax.set_ylabel("$Fréquences [Hz]$")
    ax.set_zlabel("$Amplitudes$")
    fig.colorbar(surface, shrink=0.6)
    positions_etiquettes = np.log2(etiquettes)
    ax.yaxis.set_major_locator(FixedLocator(positions_etiquettes))
    ax.yaxis.set_major_formatter(FixedFormatter([f"{i:g}" for i in etiquettes]))
    ax.yaxis.set_minor_formatter(NullFormatter())

if __name__ == "__main__":
    gen_plot_3D("Steinway1")
    plt.show()

