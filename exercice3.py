import itertools

def count_ways_to_get_sum(target_sum, num_dice=5, num_faces=6):
    """
    Calcule le nombre de façons différentes d'obtenir une somme cible avec les dés.

    Args:
    - target_sum (int): La somme cible à obtenir.
    - num_dice (int): Le nombre de dés (par défaut 5).
    - num_faces (int): Le nombre de faces par dé (par défaut 6).

    Returns:
    - int: Le nombre de façons d'obtenir la somme cible.
    """
    # Créer la liste des valeurs possibles pour un dé (1 à num_faces)
    dice_faces = list(range(1, num_faces + 1))
    
    # Générer toutes les combinaisons possibles pour les num_dice dés
    combinations = itertools.product(dice_faces, repeat=num_dice)
    
    # Initialiser le compteur de combinaisons valides
    count = 0
    
    # Parcourir toutes les combinaisons et vérifier si la somme est égale à target_sum
    for combo in combinations:
        if sum(combo) == target_sum:
            count += 1
    
    return count

def main():
    """
    Fonction principale qui demande à l'utilisateur la somme cible et
    affiche le nombre de façons d'obtenir cette somme avec 5 dés.
    """
    print("Bienvenue dans le programme de calcul des façons d'obtenir une somme avec des dés !")
    
    # Demander à l'utilisateur d'entrer une somme cible
    while True:
        try:
            target_sum = int(input("\nVeuillez entrer la somme cible à obtenir (par exemple, 20) : "))
            if target_sum < 5 or target_sum > 30:  # Vérification que la somme est raisonnable (5 à 30 pour 5 dés)
                print("La somme cible doit être comprise entre 5 et 30 pour 5 dés. Essayez à nouveau.")
            else:
                break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    # Calculer le nombre de façons d'obtenir la somme cible avec 5 dés
    ways = count_ways_to_get_sum(target_sum)

    # Afficher le résultat de manière claire et professionnelle
    print(f"\nIl existe {ways} façons différentes d'obtenir la somme {target_sum} avec 5 dés.")

if __name__ == "__main__":
    main()
