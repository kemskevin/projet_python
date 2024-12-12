
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv("classsification_log.csv", header=None, names=["timestamp", "user_id", "file_path"])

# Convertir la colonne "timestamp" en format datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extraire le nom du fichier
df["file_name"] = df["file_path"].str.extract(r'([^/]+$)')

# Créer un histogramme du nombre de requêtes par heure
df['heure'] = pd.to_datetime(df['timestamp']).dt.hour
df['heure'].hist()
plt.show()