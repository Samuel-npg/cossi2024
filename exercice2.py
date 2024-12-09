import matplotlib.pyplot as plt
import numpy as np

def draw_circle(radius):
    # Créer les coordonnées du cercle
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Créer une figure et un axe
    fig, ax = plt.subplots()

    # Tracer le cercle
    ax.plot(x, y)

    # Définir le titre et les labels
    ax.set_title(f"Cercle avec rayon {radius}")
    ax.set_xlabel("Axe X")
    ax.set_ylabel("Axe Y")
    
    # Ajuster l'échelle pour que le cercle soit bien proportionné
    ax.set_aspect('equal', 'box')
    ax.grid(True)

    # Afficher le cercle
    plt.show()

# Demander à l'utilisateur de saisir le rayon du cercle
try:
    print("Veuillez entrer le rayon du cercle :")
    radius = float(input())  # Saisie du rayon (en nombre réel)

    if radius <= 0:
        print("Le rayon doit être positif.")
    else:
        draw_circle(radius)

except ValueError:
    print("Erreur : Vous devez entrer un nombre valide pour le rayon.")
