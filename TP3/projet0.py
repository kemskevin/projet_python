import os
import shutil
import logging

# Configuration du fichier de log
logging.basicConfig(
    filename="classification_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Demander le chemin du répertoire source
repertoire_source = input("Entrez le chemin du répertoire source : ")

# Vérification si le répertoire existe
if not os.path.exists(repertoire_source):
    logging.error(f"Le répertoire {repertoire_source} n'existe pas.")
    print("Erreur : Répertoire introuvable.")
    exit()
    
# Création des sous-dossiers et classification
def classer_fichiers(repertoire):
    try:
        fichiers = os.listdir(repertoire)
        for fichier in fichiers:
            chemin_fichier = os.path.join(repertoire, fichier)

            # Ignorer les répertoires
            if os.path.isdir(chemin_fichier):
                continue

            # Identifier l'extension du fichier
            _, extension = os.path.splitext(fichier)
            extension = extension[1:].lower()  # Supprimer le point et mettre en minuscule

            # Créer le sous-dossier si nécessaire
            sous_dossier = os.path.join(repertoire, extension)
            if not os.path.exists(sous_dossier):
                os.makedirs(sous_dossier)

            # Déplacer le fichier dans le sous-dossier
            destination = os.path.join(sous_dossier, fichier)
            shutil.move(chemin_fichier, destination)
            logging.info(f"Fichier déplacé : {chemin_fichier} -> {destination}")
        print("Classification terminée avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la classification : {e}")
        print("Une erreur est survenue.")
        

# Résumé des actions
def generer_resume(repertoire):
    try:
        extensions = [d for d in os.listdir(repertoire) if os.path.isdir(os.path.join(repertoire, d))]
        logging.info("Résumé des fichiers déplacés :")
        for ext in extensions:
            chemin_dossier = os.path.join(repertoire, ext)
            nombre_fichiers = len(os.listdir(chemin_dossier))
            logging.info(f"Extension .{ext} : {nombre_fichiers} fichiers")
    except Exception as e:
        logging.error(f"Erreur lors de la génération du résumé : {e}")
        

if __name__ == "__main__":
    classer_fichiers(repertoire_source)
    generer_resume(repertoire_source)
    print("Le fichier de log 'classification_log.txt' a été créé.")