import numpy as np

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
    indices_trie_0 = np.argsort(vecteurs[:, 0])
    indices_trie_1 = np.argsort(vecteurs[:, 1])
    vecteurs_ordre_lex_1=vecteurs[indices_trie_0]
    vecteurs_ordre_lex_2=vecteurs[indices_trie_1]
    vecteurs_pareto_opti=[]
    best_lex_2=vecteurs_ordre_lex_2[0]
    for v in vecteurs_ordre_lex_1:
        if v[0] <= best_lex_2[0]:
            vecteurs_pareto_opti.append(v)
        else:
            break
    
    return vecteurs_pareto_opti



# Exemple d'utilisation :
vecteurs=generer_vecteurs_normaux(5,10)
print(vecteurs)
pareto_optimals = ordre_lex_pareto(vecteurs)
print(pareto_optimals)