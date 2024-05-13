def armstrongNumber(num):
    chiffre = str(num)
    lenght = len(chiffre)
    somme = 0

    for chf in chiffre:
        somme += int(chf) ** lenght
    
    if somme == num:
        return True
    else:
        return False
    
number = int(input("Entrez un nombre : "))

if armstrongNumber(number) and len(str(number)) == 3:
    print(f"{number} est un nombre Armstrong.")
else:
    print(f"{number} n'est pas un nombre Armstrong")
