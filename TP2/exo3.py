def majuscule_mot(chaine):
    mots = chaine.split()
    mots_maj = [mot.capitalize() for mot in mots]
    return " ".join(mots_maj)

a = input("entrer votre phrase: ")

resultat = majuscule_mot(a)
print(resultat)
