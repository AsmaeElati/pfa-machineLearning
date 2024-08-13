import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données depuis le fichier uploadé avec le bon encodage et séparateur
file_path = 'Final_Avito_Dataset.csv'
data = pd.read_csv(file_path, sep=',', encoding='latin1')

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
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_columns) == 0:
    st.error("Aucune colonne numérique disponible pour l'analyse.")
else:
    selected_column = st.selectbox('Sélectionnez une colonne pour identifier les outliers:', numeric_columns)

    if selected_column:
        st.subheader(f'Box Plot de {selected_column}')
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data[selected_column])
        st.pyplot(plt)

        Q1 = data[selected_column].quantile(0.25)
        Q3 = data[selected_column].quantile(0.75)
        IQR = Q3 - Q1

        outliers = data[(data[selected_column] < (Q1 - 1.5 * IQR)) | (data[selected_column] > (Q3 + 1.5 * IQR))]

        st.subheader(f'Outliers détectés dans {selected_column}')
        st.write(outliers)
        st.write(f'Nombre total d\'outliers dans {selected_column}: {len(outliers)}')

# Heatmap des corrélations
st.header('Heatmap des Corrélations')

if len(numeric_columns) > 0:
    corr = data[numeric_columns].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot(plt)
else:
    st.error("Aucune colonne numérique disponible pour la heatmap des corrélations.")

# Scatter Plot entre deux colonnes
if len(numeric_columns) > 1:
    st.header('Scatter Plot entre Deux Colonnes')
    col1 = st.selectbox('Sélectionnez la première colonne:', numeric_columns)
    col2 = st.selectbox('Sélectionnez la deuxième colonne:', numeric_columns)

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
    file_name='Final_Avito_Dataset.csv',
    mime='text/csv',
)
