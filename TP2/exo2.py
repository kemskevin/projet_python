def premierMot(chaine):
    mot = chaine.split()
    return mot[0] if mot else ""

a = input("entrer votre phrase: ")
b = premierMot(a)
print("le premier mot de cette phrase est: ",b)