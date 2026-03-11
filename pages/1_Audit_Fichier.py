import streamlit as st
import pandas as pd
import joblib

st.title("⚡ Centre de Décision Opérationnel")

model = joblib.load('models/modele_fraude.pkl')

uploaded_file = st.file_uploader("Importer le flux de transactions entrantes (CSV)", type="csv")

if uploaded_file:
    df_new = pd.read_csv(uploaded_file)
    
    # On définit les colonnes que l'IA attend (V1-V28, Hour, Amount_Scaled)
    features = [f'V{i}' for i in range(1, 29)] + ['Hour', 'Amount_Scaled']
    
    if all(col in df_new.columns for col in features):
        if st.button("Lancer le filtrage de sécurité"):
            preds = model.predict(df_new[features])
            df_new['Decision'] = ["🛑 BLOQUER" if p == 1 else "✅ APPROUVER" for p in preds]
            
            # Affichage des alertes
            fraudes = df_new[df_new['Decision'] == "🛑 BLOQUER"]
            if not fraudes.empty:
                st.error(f"Alerte : {len(fraudes)} tentatives de fraude détectées !")
                st.dataframe(fraudes)
            else:
                st.success("Toutes les transactions sont conformes.")
    else:
        st.warning("Erreur : Le fichier doit contenir les colonnes V1 à V28.")