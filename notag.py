import pandas as pd

# Charger le dataset
path = "./archive/medium_articles.csv"
df = pd.read_csv(path, delimiter=",", quotechar='"')

# Vérifier les valeurs vides ou des listes vides dans la colonne 'tags'
empty_tags_count = df[df['tags'].isna() | (df['tags'] == '[]')].shape[0]

print(f"Nombre d'objets avec une liste de tags vide : {empty_tags_count}")
