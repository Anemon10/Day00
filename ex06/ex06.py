def myLenght(chaine):
    count = 0
    for character in chaine:
        count += 1
    return count

texte = "Bonjour le monde !"
longueur_texte = myLenght(texte)
print(f"Ce texte contient {longueur_texte} caractères, espaces compris.")