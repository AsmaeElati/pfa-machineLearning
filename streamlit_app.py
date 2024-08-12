import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
file_path = 'Final_Avito_Dataset.csv'
data = pd.read_csv(file_path)

# Titre de l'application
st.title('Analyse et Visualisation du Dataset Avito')

# Aperçu des données
st.header('Aperçu des Données')
st.write(data.head())

# Statistiques descriptives
st.header('Statistiques Descriptives')
st.write(data.describe())

# Sélection d'une colonne pour l'analyse des outliers
st.header('Détection des Outliers')
selected_column = st.selectbox('Sélectionnez une colonne pour identifier les outliers:', data.select_dtypes(include=['float64', 'int64']).columns)

# Box Plot pour la colonne sélectionnée
st.subheader(f'Box Plot de {selected_column}')
plt.figure(figsize=(10, 6))
sns.boxplot(x=data[selected_column])
st.pyplot(plt)

# Calcul des outliers en utilisant l'IQR
Q1 = data[selected_column].quantile(0.25)
Q3 = data[selected_column].quantile(0.75)
IQR = Q3 - Q1

outliers = data[(data[selected_column] < (Q1 - 1.5 * IQR)) | (data[selected_column] > (Q3 + 1.5 * IQR))]

st.subheader(f'Outliers détectés dans {selected_column}')
st.write(outliers)

# Affichage du nombre d'outliers détectés
st.write(f'Nombre total d\'outliers dans {selected_column}: {len(outliers)}')

# Heatmap des corrélations
st.header('Heatmap des Corrélations')

# Filtrer uniquement les colonnes numériques
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Gérer les valeurs manquantes en les remplissant par la médiane (ou toute autre stratégie)
numeric_data = numeric_data.fillna(numeric_data.median())

# Calculer la matrice de corrélation
corr = numeric_data.corr()

# Afficher la heatmap des corrélations
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
st.pyplot(plt)

# Scatter plot entre deux colonnes
st.header('Scatter Plot entre Deux Colonnes')
col1 = st.selectbox('Sélectionnez la première colonne:', numeric_data.columns)
col2 = st.selectbox('Sélectionnez la deuxième colonne:', numeric_data.columns)

st.subheader(f'Scatter Plot entre {col1} et {col2}')
plt.figure(figsize=(10, 6))
sns.scatterplot(x=numeric_data[col1], y=numeric_data[col2])
st.pyplot(plt)

# Analyse de regroupement
st.header('Analyse de Regroupement')
group_by_column = st.selectbox('Sélectionnez une colonne pour regrouper les données:', data.columns)
grouped_data = data.groupby(group_by_column).size().reset_index(name='Counts')

st.subheader(f'Nombre d\'occurrences par {group_by_column}')
st.bar_chart(grouped_data.set_index(group_by_column))

# Afficher l'ensemble du dataset
if st.checkbox('Afficher l\'ensemble des données'):
    st.write(data)

# Lien de téléchargement pour le dataset
st.header('Télécharger le Dataset')
st.download_button(
    label="Télécharger les données en CSV",
    data=data.to_csv().encode('utf-8'),
    file_name='Avito_Dataset.csv',
    mime='text/csv',
)
