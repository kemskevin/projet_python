"""Vérifions si une chaîne est un palindrome."""
chaine = input("Entrez un mot : ")
#chaine = chaine.lower()  # On met tout en minuscules pour ignorer la casse
if chaine == chaine[::-1]:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
