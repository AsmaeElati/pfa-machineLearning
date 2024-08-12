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

# Sélection de colonnes pour l'analyse
st.header('Analyse de la Distribution d\'une Colonne')
selected_column = st.selectbox('Sélectionnez une colonne pour afficher sa distribution:', data.columns)

# Distribution de la colonne sélectionnée
st.subheader(f'Distribution de {selected_column}')
plt.figure(figsize=(10, 6))
sns.histplot(data[selected_column], kde=True, bins=30)
st.pyplot(plt)

# Box plot pour détecter les outliers
st.header('Box Plot')
selected_column_boxplot = st.selectbox('Sélectionnez une colonne pour afficher un box plot:', data.columns)

st.subheader(f'Box Plot de {selected_column_boxplot}')
plt.figure(figsize=(10, 6))
sns.boxplot(x=data[selected_column_boxplot])
st.pyplot(plt)

# Heatmap des corrélations
st.header('Heatmap des Corrélations')
corr = data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
st.pyplot(plt)

# Scatter plot entre deux colonnes
st.header('Scatter Plot entre Deux Colonnes')
col1 = st.selectbox('Sélectionnez la première colonne:', data.columns)
col2 = st.selectbox('Sélectionnez la deuxième colonne:', data.columns)

st.subheader(f'Scatter Plot entre {col1} et {col2}')
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data[col1], y=data[col2])
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
