import random

taille = 15
tableau_aléa = [random.randint(1, 100) for _ in range(taille)]

def tri_décroissant(tableau):
    for i in range (1, len(tableau)):
        for j in range (i+1, len(tableau)):
            if tableau[i] < tableau[j]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau


print(tableau_aléa)
tableau_trié = tri_décroissant(tableau_aléa)
print(f"voici le tableau trié : {tableau_trié}")