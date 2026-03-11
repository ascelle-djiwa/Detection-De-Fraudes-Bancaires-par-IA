# Détection de fraudes bancaires par IA
# Présentation du Projet
Ce projet propose une solution logicielle complète pour l'identification de transactions frauduleuses. Il ne s'agit pas seulement d'un modèle d'IA, mais d'une architecture logicielle intégrant un pipeline de données (ETL) et une interface décisionnelle métier.

# Architecture du Système
Le projet est divisé en trois composants majeurs respectant les principes de séparation des responsabilités :

1. **Le Laboratoire** : Exploration des données (EDA), ingénierie des caractéristiques et entraînement de deux modèles Random Forest (Expert vs Simple).

2. **Le Pipeline ETL** : Script d'automatisation chargé du nettoyage, de la normalisation (RobustScaler) et de la transformation des données brutes en données exploitables.

3. **L'Interface Décisionnelle** : Application Web multi-pages permettant aux analystes de traiter des fichiers de masse ou de simuler des transactions isolées.

## Résultats
* **Modèle Expert** : Rappel de 83% (détection efficace des fraudes complexes).
  ![Résultats du modèle expert](images/ResultatEvaluationModele.png)
* **Modèle Simplifié** : Utilisé pour la simulation rapide sur données restreintes.
![Résultats du modèlesimplifié](images/ResultatEvaluationModeleSimplifie.png)
## Installation
1. Installez les dépendances : `pip install pandas scikit-learn matplotlib seaborn streamlit joblib` ou faites `pip install -r requirements.txt`
2. Lancez le pipeline : `python pipeline.py`
3. Lancez l'application : `streamlit run app.py`

**Plus d'informations dans Documentation_Technique.md**
