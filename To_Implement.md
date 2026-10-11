## Théorie
- Trouver sur quel nombre de données rouler la FFT pour obtenir une précision correcte, en fonction du pas de temps d'acquisition de données.
- Trouver si la FFT doit être roulée sur les données forward, backward ou middle.
- Trouver la précision en fréquences (vecteur de longueur $k$) lorsque j'ai un vecteur temporel de longueur $n$. 

## Calculs
- Importer scipy
- FFT sur une bande d'Amplitudes sonores par rapport au temps. Prend en entrée les bornes temporelles, découpe les données temporelles, roule la FFT puis exporte les données fréquentielles
- Trouver les maximums locaux (hamoniques)
- Export des données fréquentielles dans une matrice ou tableau pandas. Avec un indice qui indique le temps t où a été calculé ce spectre fréquentiel


## Features
- Graphique 3D des spectres de fréquences en amplitude selon le temps.
- Curseurs pour modifier les paramètres suivants: temps total pour la FFT, autres.

