def pyramide(n):
    for i in range(1, n+1):
        espaces = " " * (n-i)
        étoile = "*" * (2 * i - 1)
        print(espaces + étoile)

while True:
    try:
        number_line = int(input("Combien de lignes à votre pyramide ? "))
        if number_line <= 0:
            raise ValueError
        break
    except ValueError:
        print("Veuillez entrer un entier positif.")

pyramide(number_line)