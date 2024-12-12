def image(mot):
    resultat = ""
    i = 0
    while i < len(mot):
        count = 1
        while i + 1 < len(mot) and mot[i] == mot[i + 1]:
            i += 1
            count += 1
        resultat += str(count) + mot[i]
        i += 1
    return resultat

def suite_conway(n):
    terme = "1"
    print(f"u0 = {terme}")
    for i in range(1, n):
        terme = image(terme)
        print(f"u{i} = {terme}")

# Exemple d'utilisation
suite_conway(20)