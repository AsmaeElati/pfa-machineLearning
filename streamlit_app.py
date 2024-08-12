import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
file_path = 'Final_Avito_Dataset.csv'
data = pd.read_csv(file_path)

# Filtrer uniquement les colonnes numériques
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Gérer les valeurs manquantes en les remplissant par la médiane (ou toute autre stratégie)
numeric_data = numeric_data.fillna(numeric_data.median())

# Calculer la matrice de corrélation
st.header('Heatmap des Corrélations')
corr = numeric_data.corr()

# Afficher la heatmap des corrélations
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
st.pyplot(plt)
