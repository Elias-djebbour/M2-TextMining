import os
import pandas as pd
import xml.etree.ElementTree as ET

# Dossier contenant les fichiers XML
dossier_xml = "xml/compteRendu"

# Dictionnaire de classification élargi des thèmes
classification_themes = {
    "santé": ["prévention", "santé publique", "maladies", "hôpital", "sport", "soins", "médical", "vaccin"],
    "économie": ["finance", "budget", "économie", "chômage", "entreprises", "impôts", "fiscalité", "commerce"],
    "éducation": ["éducation", "école", "université", "formation", "enseignants", "étudiants", "enseignement"],
    "immigration": ["migrants", "asile", "réfugiés", "immigration", "frontières", "intégration"],
    "environnement": ["écologie", "environnement", "climat", "pollution", "énergie", "biodiversité", "développement durable"],
    "droit": ["justice", "lois", "code", "constitution", "droit", "tribunal", "juridique", "législation"],
    "sécurité": ["sécurité", "police", "gendarmerie", "armée", "terrorisme", "criminalité", "cybersécurité"],
    "culture": ["culture", "patrimoine", "arts", "cinéma", "musique", "livres", "langue", "tourisme"],
    "technologie": ["technologie", "numérique", "internet", "innovation", "recherche", "cybersécurité", "intelligence artificielle"],
    "agriculture": ["agriculture", "pêche", "ruralité", "élevage", "fermes", "paysan", "produits agricoles"],
    "social": ["social", "famille", "inégalités", "pauvreté", "solidarité", "logement", "exclusion", "handicap"],
    "travail": ["travail", "emploi", "salaires", "syndicats", "conditions de travail", "licenciements", "grèves"],
    "transport": ["transport", "mobilité", "infrastructure", "routes", "trains", "aviation", "logistique"],
    "défense": ["défense", "armée", "militaire", "guerre", "conflits", "stratégie"],
    "politique": ["politique", "gouvernement", "élections", "partis", "assemblée", "président", "députés", "réformes"],
    "autre": []  # Tous les thèmes non classés
}

# Fonction pour classifier un thème
def classifier_theme(titre):
    titre = titre.lower()
    for theme, mots_cles in classification_themes.items():
        if any(mot in titre for mot in mots_cles):
            return theme
    return "autre"  # Si aucun mot-clé ne correspond

# Liste pour stocker les données
data = []

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(dossier_xml):
    if fichier.endswith(".xml"):
        chemin_fichier = os.path.join(dossier_xml, fichier)
        
        # Lire le fichier XML
        tree = ET.parse(chemin_fichier)
        root = tree.getroot()
        
        # Extraire le namespace (espace de noms)
        namespace = {"ns": root.tag.split('}')[0].strip('{')}
        
        # Trouver les thèmes dans le fichier
        themes = root.findall(".//ns:intitule", namespaces=namespace)
        
        # Classifier les thèmes
        liste_themes = [classifier_theme(theme.text.strip()) for theme in themes if theme.text]
        
        # Ajouter au DataFrame
        data.append({"nom_fichier": fichier, "themes": list(set(liste_themes))})  # Retirer doublons avec `set`

# Créer un DataFrame
df = pd.DataFrame(data)

# Afficher le DataFrame
print(df)

# Sauvegarder le DataFrame dans un fichier CSV si besoin
df.to_csv("themes_classifies.csv", index=False)
