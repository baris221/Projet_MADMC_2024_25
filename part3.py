from part1 import generer_vecteurs_normaux, is_dominated, get_pareto_optimals
from part2 import find_minimax, deux_etapes_procedures
import matplotlib.pyplot as plt
import time

def transform_instance(vecteurs, alpha_min, alpha_max):
    """
    Transforme une instance du problème I-dominance en une instance de dominance de Pareto.

    Args:
        points (list of tuples): Liste des points d'origine, où chaque point est un tuple (y1, y2).
        alpha_min (float): Borne inférieure de l'intervalle I.
        alpha_max (float): Borne supérieure de l'intervalle I.

    Returns:
        list of tuples: Liste des points transformés pour Pareto dominance.
    """
    transformed_points = []
    for y1, y2 in vecteurs:
        y_min = (alpha_min * y1 + (1 - alpha_min) * y2, y2)
        y_max = (alpha_max * y1 + (1 - alpha_max) * y2, y2)
        transformed_points.extend([y_min, y_max])
    return transformed_points

def calculate_image(vecteurs, alpha_min, alpha_max):
    vecteurs_results = get_pareto_optimals(vecteurs)
    minimax = find_minimax(vecteurs_results, alpha_min, alpha_max)
    return minimax

def I_dominance_vers_pareto(vecteurs_I_domines, alpha_min, alpha_max):
    transformed_points = transform_instance(vecteurs_I_domines, alpha_min, alpha_max)
    return calculate_image(transformed_points, alpha_min, alpha_max)



def is_dominated_pi_prime(v,vecteurs,alpha_min,alpha_max):
    for vecteur in vecteurs:
            if (alpha_min*vecteur[0]+(1-alpha_min)*vecteur[1] < alpha_min*v[0]+(1-alpha_min)*v[1]) and (alpha_max*vecteur[0]+(1-alpha_max)*vecteur[1] < alpha_max*v[0]+(1-alpha_max)*v[1]):
                return True
    return False

def get_non_I_dominated_vectors(vecteurs,alpha_min,alpha_max):
    vecteurs_non_I_domines=[]
    for vecteur in vecteurs:
        if not is_dominated_pi_prime(vecteur,vecteurs,alpha_min,alpha_max):
            vecteurs_non_I_domines.append(vecteur)
    
    return vecteurs_non_I_domines

def deux_etapes_procedures_deux(vecteurs,alpha_min,alpha_max):
    vecteurs_non_domines=get_non_I_dominated_vectors(vecteurs,alpha_min,alpha_max)
    #print(vecteurs_non_domines)
    point_minimax=find_minimax(vecteurs_non_domines,alpha_min,alpha_max)
    return point_minimax

def pareto_vers_I_dominance(vecteurs_pareto, alpha_min, alpha_max):
    vecteurs = get_non_I_dominated_vectors(vecteurs_pareto, alpha_min, alpha_max)
    return find_minimax(vecteurs,alpha_min,alpha_max)

if __name__=="__main__":
    n = 50
    m = 1000
    vecteurs=generer_vecteurs_normaux(n,m)
    k = 10
    eps = 0.025

    eps_values = []
    for i in range(20):
        eps_values.append(eps)
        eps += 0.025
        eps = round(eps, 3)

    #print(eps_values)
    num_instances = 50

    times_procedure_un = []
    times_procedure_deux = []

    for eps in eps_values:
        I_eps_min = 0.5 - eps
        I_eps_max = 0.5 + eps
    
        time_un = 0
        time_deux = 0
    
        for _ in range(num_instances):
            vecteurs = generer_vecteurs_normaux(n, m)
        
            start_time = time.time()
            deux_etapes_procedures(vecteurs, k, I_eps_min, I_eps_max)
            time_un += time.time() - start_time
        
            start_time = time.time()
            deux_etapes_procedures_deux(vecteurs, I_eps_min, I_eps_max)
            time_deux += time.time() - start_time
    
        times_procedure_un.append(time_un / num_instances)
        times_procedure_deux.append(time_deux / num_instances)

    plt.plot(eps_values, times_procedure_un, label='Procedure Un',marker='o')
    plt.plot(eps_values, times_procedure_deux, label='Procedure Deux',marker='x')
    plt.xlabel('Epsilon')
    plt.ylabel('Average Execution Time (s)')
    plt.title("Comparaison de temps d'éxecution de deux procédures")
    plt.legend()
    plt.grid()
    plt.show()

