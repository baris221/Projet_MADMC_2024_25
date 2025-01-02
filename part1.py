import numpy as np
import time
import matplotlib.pyplot as plt

def generer_vecteurs_normaux(n,m):
    """
    Génère un ensemble de n vecteurs avec des composantes tirées aléatoirement selon une loi normale.

    Paramètres :
    - n (int) : Nombre de vecteurs à générer.
    - dim (int) : Dimension de chaque vecteur.
    - m (float) : Espérance de la loi normale.

    Retour :
    - np.ndarray : Tableau de forme (n, 2) contenant les vecteurs générés.
    """
    ecart_type = m / 4  # Calcul de l'écart-type
    vecteurs = np.random.normal(loc=m, scale=ecart_type, size=(n,2))
    return vecteurs


def is_dominated(v,vecteurs):
    """
    Renvoie True si le vecteur v est pareto-opti par rapport aux vecteurs.

    Paramètres:
    - v (np.ndarray) : Vecteur à tester.
    - vecteurs (np.ndarray) : Ensemble de vecteurs.

    Retour:
    - bool: True si v est pareto-opti, False sinon.
    """
    for vecteur in vecteurs:
        if (vecteur[0]<v[0] and vecteur[1]<v[1]) or (vecteur[0]<=v[0] and vecteur[1]<v[1]) or (vecteur[0]<v[0] and vecteur[1]<=v[1]) :
            return True
    
    return False

def get_pareto_optimals(vecteurs):
    """
    Renvoie des ensembles des vecteurs pareto-optimaux
    
    Paramètres:
    - vecteurs (np.ndarray) : Ensemble de vecteurs.

    Retour:
    - list: Liste de listes contenant les vecteurs pareto-optimaux.
    """
    vecteurs_pareto_opti=[]
    for vecteur in vecteurs:
        if not is_dominated(vecteur,vecteurs):
            vecteurs_pareto_opti.append(vecteur)
    
    return vecteurs_pareto_opti

def ordre_lex_pareto(vecteurs):
    """"""
    indices_trie = np.argsort(vecteurs[:, 0])
    vecteurs_ordre = vecteurs[indices_trie]
    vecteurs_pareto_opti = []
    meilleur_y = float('inf')
    for v in vecteurs_ordre:
        if v[1] < meilleur_y:
            vecteurs_pareto_opti.append(v)
            meilleur_y = v[1]
    return vecteurs_pareto_opti


if __name__=="__main__":
    # Comparaison expérimentale
    n_values = range(200, 10001, 200)
    m = 1000
    iterations = 50

    temps_algo1 = []  # Pour l'algorithme basé sur `is_dominated`
    temps_algo2 = []  # Pour l'algorithme basé sur `ordre_lex_pareto`

    for n in n_values:
        temps1 = []
        temps2 = []
        for _ in range(iterations):
            vecteurs = generer_vecteurs_normaux(n, m)

            # Temps pour le premier algorithme
            start = time.time()
            list1=get_pareto_optimals(vecteurs)
            temps1.append(time.time() - start)

            # Temps pour le second algorithme
            start = time.time()
            list2=ordre_lex_pareto(vecteurs)
            temps2.append(time.time() - start)
        # Moyenne des temps d'exécution
        temps_algo1.append(np.mean(temps1))
        temps_algo2.append(np.mean(temps2))

    # Tracé des résultats
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, temps_algo1, label='Algorithme basé sur is_dominated', marker='o')
    plt.plot(n_values, temps_algo2, label='Algorithme basé sur ordre_lex_pareto', marker='x')
    plt.xlabel('Nombre de vecteurs (n)')
    plt.ylabel('Temps moyen (secondes)')
    plt.title('Comparaison des temps d\'exécution des deux algorithmes')
    plt.legend()
    plt.grid()
    plt.show()