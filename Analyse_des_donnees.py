from FFT import gen_data_for_3D, DT, K, FREQ
import matplotlib.pyplot as plt

F_INT = [220 * 2**i for i in range(7)]
NOM_PIANO = "Erard1"

donnees = gen_data_for_3D(piano_name=NOM_PIANO)

def cibler_donnees(frequence_d_interet:float):
    df = 1 / (DT * K)
    i = round(frequence_d_interet / df)
    t = temps = donnees["Temps"]
    ampl = evolution_temporelle_freq_interet = [vecteur[i] for vecteur in donnees["Amplitudes"]]
    return t, ampl


def gen_all_harmonics_graph():
    for f in F_INT: 
        t, ampl = cibler_donnees(frequence_d_interet=f)
        plt.plot(t, ampl, label=f"$f={f}$ Hz")
        plt.xlabel("Temps $[s]$")
        plt.ylabel("Log(amplitude)")
        plt.legend()
        plt.grid()
    plt.show()

gen_all_harmonics_graph()
       
    



