import pandas as pd

# Charger le dataset
path = "./archive/medium_articles.csv"
df = pd.read_csv(path, delimiter=",", quotechar='"')

# Vérifier les valeurs vides ou des listes vides dans la colonne 'tags'
empty_text_count = df[df['text'].isna() | (df['text'] == '')].shape[0]

print(f"Nombre d'objets avec une liste de text vide : {empty_text_count}")