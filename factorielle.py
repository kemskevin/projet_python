def factorielle(n):
    """Fonction qui permet le calcul du factorielle d'un nombre n de manière récursive."""
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Entrez un nombre : "))

# Calcul et affichage de la factorielle
resultat = factorielle(nombre)
print("La factorielle de", nombre, "est", resultat)
