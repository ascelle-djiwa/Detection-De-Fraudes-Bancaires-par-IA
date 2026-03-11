import pandas as pd
from sklearn.preprocessing import RobustScaler
import os #Utilisez os pour forcer le programme à chercher le fichier dans le bon dossier pour la fonction run_pipeline()

def extract_data(file_path):
    print(f"--- 📥 Extraction : {file_path} ---")
    return pd.read_csv(file_path)

def transform_data(df):
    print("--- ⚙️ Transformation (Engineering) ---")
    
    # 1. Création de la variable temporelle
    df['Hour'] = (df['Time'] // 3600) % 24
    
    # 2. Mise à l'échelle robuste du montant
    scaler = RobustScaler()
    df['Amount_Scaled'] = scaler.fit_transform(df[['Amount']])
    
    # 3. Sélection et réorganisation stricte des colonnes
    #Remarque perso : L'ordre doit être identique à celui de l'entraînement
    v_cols = [f'V{i}' for i in range(1, 29)]
    target_col = ['Class'] if 'Class' in df.columns else []
    
    final_cols = v_cols + ['Hour', 'Amount_Scaled'] + target_col
    
    return df[final_cols]

def run_pipeline():
    # Cette ligne récupère le chemin du dossier où est enregistré pipeline.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Construction du chemin complet vers le fichier
    input_p = os.path.join(base_path, 'data/brut/creditcard.csv')
    output_p = os.path.join(base_path, 'data/propre/creditcard_clean.csv')
    
    print(f"🔍 Recherche du fichier dans : {input_p}")
    
    if not os.path.exists(input_p):
        print(f"❌ Erreur : Le fichier est introuvable à l'adresse indiquée.")
        return

    try:
        raw_data = extract_data(input_p)
        clean_data = transform_data(raw_data)
        
        clean_data.to_csv(output_p, index=False)
        print(f"✅ Succès ! '{output_p}' a été créé dans le dossier.")
    except Exception as e:
        print(f" Une erreur est survenue : {e}")
if __name__ == "__main__":
    run_pipeline()