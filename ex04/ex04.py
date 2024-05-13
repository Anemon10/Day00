import random

taille = 15
tableau_aléa = [random.randint(1, 100) for _ in range(taille)]

def tri_croissant(tableau):
    for i in range(1, len(tableau)):
        valeur = tableau[i]
        position = i

        while position > 0 and tableau[position - 1] > valeur:
            tableau[position] = tableau[position - 1]
            position -= 1

        tableau[position] = valeur

    return tableau
    
print(tableau_aléa)    
tableau_trié = tri_croissant(tableau_aléa)
print(f"voici le tableau trié : {tableau_trié}")
