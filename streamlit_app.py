import streamlit as st
import pandas as pd
# Streamlit app layout
st.title('CSV Data Viewer')

st.write('This app loads and displays data from a CSV file.')

# Path to the local CSV file
file_path = 'Final_Avito_Dataset.csv'  # Update with your local file path
data_cleaned = pd.read_csv(file_path, sep=';')

# Afficher un aperçu des données
data_cleaned.head()

