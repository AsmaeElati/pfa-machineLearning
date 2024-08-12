import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données depuis le fichier uploadé
file_path = 'Final_Avito_Dataset.csv'
data = pd.read_csv(file_path)

st.title('Analyse et Visualisation du Dataset Avito')

st.header('Aperçu des Données')
st.write(data.head())

# Vérifier les colonnes numériques
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_columns) == 0:
    st.error("Aucune colonne numérique disponible pour l'analyse.")
else:
    st.header('Détection des Outliers')
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
