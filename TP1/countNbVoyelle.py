"""Comptons le nombre de voyelles dans une phrase."""
phrase = input("Entrez une phrase: ")
voyelles = "aeiouAEIOU"  # On inclut les voyelles majuscules
compteur = 0
for lettre in phrase:
    if lettre in voyelles:
      compteur += 1
print("Il y a", compteur, "voyelles dans la phrase.")
