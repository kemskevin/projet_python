"""Trouvons le plus grand nombre parmi un certains nombres saisis."""
a = int(input("entrer le nombre de chiffre: "))
nombres = []
for i in range(a):
    nombre = int(input("Entrez un nombre : "))
    nombres.append(nombre)
  
plus_grand = max(nombres)
print("Le plus grand nombre est :", plus_grand)
