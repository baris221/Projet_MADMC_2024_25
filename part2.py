from part1 import ordre_lex_pareto,generer_vecteurs_normaux
import numpy as np

# Programmation Dynamique

def prog_dynamique(vecteurs,k):
    n=len(vecteurs)
    table_DP=[[[] for _ in range(k+1)]for _ in range(n+1)]
    
    for i in range(n):
        table_DP[i][0]=[(0,0)]
    
    
    for i in range(1,k+1):
        table_DP[0][i]=[(v[0] + vecteurs[0][0], v[1] + vecteurs[0][1]) for v in table_DP[0][i-1]]

    for i in range(1,n+1):
        for j in range(1,k+1):
            without_i=table_DP[i-1][j]
            with_i = [(v[0] + vecteurs[i-1][0], v[1] + vecteurs[i-1][1]) for v in table_DP[i-1][j-1]]
            vecteurs_i_j=np.array(without_i+with_i)
            vecteurs_opti=ordre_lex_pareto(vecteurs_i_j)
            table_DP[i][j]=vecteurs_opti
    
    return table_DP[n][k]

def find_minimax(vecteurs,alpha_min,alpha_max):
    minimax_vecteur=None
    minimax_value=float('inf')
    
    for vecteur in vecteurs:
        f_max=alpha_max*vecteur[0]+(1-alpha_max)*vecteur[1]
        f_min=alpha_min*vecteur[0]+(1-alpha_min)*vecteur[1]
        
        f_y=max(f_max,f_min)
        
        if f_y < minimax_value:
            minimax_value=f_y
            minimax_vecteur=vecteur
    
    return minimax_vecteur

def deux_etapes_procedures(vecteurs,k,alpha_min,alpha_max):
    vecteurs_non_domines=prog_dynamique(vecteurs,k)
    print(vecteurs_non_domines)
    point_minimax=find_minimax(vecteurs_non_domines,alpha_min,alpha_max)
    
    return point_minimax


alpha_min=0.1
alpha_max=0.9
k=10
vecteurs=generer_vecteurs_normaux(50,10)

print(deux_etapes_procedures(vecteurs,k,alpha_min,alpha_max))
        