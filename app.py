import streamlit as st

st.set_page_config(page_title="Projet Fraude MIAGE", layout="wide")

st.title("🛡️ Système de Détection de Fraude Bancaire")
st.write("""
Bienvenue dans l'outil de gestion des risques. 
Utilisez le menu à gauche pour naviguer :
- **Audit Fichier** : Pour traiter un flux de nouvelles transactions et prendre des décisions de blocage.
- **Simulation** : Pour tester manuellement une combinaison Heure/Montant.
""")

st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Sécurité Bancaire IA")