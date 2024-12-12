from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Handler pour gérer les événements
class MonHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Fichier modifié : {event.src_path}")

    def on_created(self, event):
        print(f"Fichier créé : {event.src_path}")

    def on_deleted(self, event):
        print(f"Fichier supprimé : {event.src_path}")

# Fonction principale
def surveiller_repertoire(repertoire):
    event_handler = MonHandler()
    observer = Observer()
    observer.schedule(event_handler, path=repertoire, recursive=True)
    observer.start()

    try:
        print(f"Surveillance du répertoire : {repertoire}")
        while True:
            time.sleep(1)  # Garder le script actif
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Exemple d'utilisation
repertoire_cible = input("chemin_vers_votre_repertoire ")
surveiller_repertoire(repertoire_cible)


import logging

# Configurer le fichier de log
logging.basicConfig(filename="surveillance_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

class MonHandlerAvecLog(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"Fichier modifié : {event.src_path}")

    def on_created(self, event):
        logging.info(f"Fichier créé : {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"Fichier supprimé : {event.src_path}")

# Surveillance avec log
def surveiller_repertoire_avec_log(repertoire):
    event_handler = MonHandlerAvecLog()
    observer = Observer()
    observer.schedule(event_handler, path=repertoire, recursive=True)
    observer.start()

    try:
        print(f"Surveillance (avec log) du répertoire : {repertoire}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Exemple d'utilisation
surveiller_repertoire_avec_log(repertoire_cible)

import pandas as pd


# Analyser le fichier de log
def visualiser_evenements_log(fichier_log):
    logs = pd.read_csv(fichier_log, sep=" - ", header=None, engine="python", names=["timestamp", "event", "path"])
    counts = logs["event"].value_counts()

    # Graphique
    counts.plot(kind="bar", title="Événements de fichiers", color="blue")
    plt.ylabel("Nombre d'événements")
    plt.show()

# Exemple d'utilisation
visualiser_evenements_log("surveillance_log.txt")