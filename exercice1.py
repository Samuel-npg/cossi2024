# Fonction pour calculer la factorielle avec une boucle "for"
def factorial_for(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Fonction pour calculer la factorielle avec une boucle "while"
def factorial_while(n):
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

# Fonction pour afficher des messages pour les nombres de 1 à 50
def multiples_name_and_surname():
    print("\nAffichage des multiples de 1 à 50 :")
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(f"Pour le nombre {i}: HOUEGBAN Samuel")  # Multiple de 3 et de 5
        elif i % 3 == 0:
            print(f"Pour le nombre {i}: HOUEGBAN")  # Multiple de 3
        elif i % 5 == 0:
            print(f"Pour le nombre {i}: Samuel")  # Multiple de 5
        else:
            print(f"Pour le nombre {i}: {i}")  # Pas un multiple de 3 ou 5

# ====== Partie principale du programme ======
print("Bonjour! Ce programme va vous permettre de calculer la factorielle d'un nombre et d'afficher les multiples de 1 à 50.\n")

# Demander à l'utilisateur de saisir un nombre pour calculer sa factorielle
try:
    print("Veuillez saisir un nombre entier pour calculer sa factorielle (par exemple, 5) :")
    n = int(input())  # Saisie de l'utilisateur

    # Vérifier si le nombre est positif
    if n < 0:
        print("Désolé, la factorielle n'est pas définie pour les nombres négatifs.")
    else:
        # Calcul et affichage de la factorielle
        print(f"\nCalcul de la factorielle de {n} avec la méthode 'for' :")
        print(f"Factorielle de {n} avec 'for' : {factorial_for(n)}")

        print(f"\nCalcul de la factorielle de {n} avec la méthode 'while' :")
        print(f"Factorielle de {n} avec 'while' : {factorial_while(n)}")

        # Afficher les multiples de 1 à 50
        multiples_name_and_surname()

except ValueError:
    print("Erreur : Vous devez entrer un nombre entier valide.")
