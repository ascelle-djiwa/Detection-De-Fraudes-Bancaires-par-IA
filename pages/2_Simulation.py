import streamlit as st
import pandas as pd
import joblib

st.title("🧪 Simulateur de Risque Manuel")

model = joblib.load('models/modele_fraude.pkl')

h = st.slider("Heure de la transaction", 0, 23, 12)
m = st.number_input("Montant (€)", min_value=0.0, value=100.0)

if st.button("Analyser"):
    # On complète avec des zéros pour V1-V28
    input_data = {f'V{i}': [0.0] for i in range(1, 29)}
    input_data['Hour'] = [h]
    input_data['Amount_Scaled'] = [(m - 88) / 250]
    
    X_input = pd.DataFrame(input_data)
    pred = model.predict(X_input)
    
    if pred[0] == 1:
        st.error("Résultat : FRAUDE PROBABLE")
    else:
        st.success("Résultat : TRANSACTION NORMALE")