from FFT import gen_data_for_3D, DT, K, FREQ
import matplotlib.pyplot as plt
import pandas as pd
import datetime
now = datetime.datetime.now()
from pathlib import Path

FICHIER = Path("Export_donnees.xlsx")
if FICHIER.exists():
    options = {"mode": "a", "if_sheet_exists": "replace"}
else:
    options = {"mode": "w"}


F_INT = [440 + 440* i for i in range(7)]


FICHIER = Path()

def cibler_donnees(frequence_d_interet:float, data):
    df = 1 / (DT * K)   
    i = round(frequence_d_interet / df)
    t = temps = donnees["Temps"]
    ampl = evolution_temporelle_freq_interet = [vecteur[i] for vecteur in donnees["Amplitudes"]]
    return t, ampl


def gen_all_harmonics_graph(name: str, donn, writer):
    plt.figure()                      # une figure par piano
    donnees_a_exporter = {}
    for f in F_INT:
        t, ampl = cibler_donnees(frequence_d_interet=f, data=donn)
        donnees_a_exporter["Temps"] = t
        donnees_a_exporter[f"{f:.4f} Hz"] = ampl
        plt.plot(t, ampl, label=f"({f/440:.1f}) - {f} Hz")
    plt.title(name)
    plt.xlabel("Temps $[s]$")
    plt.ylabel("Log(amplitude)")
    plt.legend()
    plt.grid()

    pd.DataFrame(donnees_a_exporter).to_excel(
        writer,
        sheet_name=f"{name} - {str(now)[5:19].replace(":", "-")}",
        index=False,
    )


with pd.ExcelWriter("Export_donnees.xlsx", engine="openpyxl", **options) as writer:
    for name in ["Pleyel1", "Erard1", "Steinway1"]:
        donnees = gen_data_for_3D(piano_name=name)
        gen_all_harmonics_graph(name, donn=donnees, writer=writer)

plt.show()





