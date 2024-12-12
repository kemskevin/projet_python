def retournePhrase(chaine):
    a = chaine.split()
    b = a[::-1]
    return " ".join(b)

a = input("entrer votre phrase à retourner: ")
b = retournePhrase(a)
print("la phrase: ", a ,"\n voici sa version retourner: ", b)
