from part1 import generer_vecteurs_normaux
from part2 import find_minimax

def is_dominated_pi_prime(v,vecteurs,alpha_min,alpha_max):
    for vecteur in vecteurs:
        for alpha in (alpha_min,alpha_max):
            if (alpha*vecteur[0]+(1-alpha)*vecteur[1] < alpha*v[0]+(1-alpha)*v[1]):
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


alpha_min=0.1
alpha_max=0.9
vecteurs=generer_vecteurs_normaux(50,10)

print(deux_etapes_procedures_deux(vecteurs,alpha_min,alpha_max))

