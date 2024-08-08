import streamlit as st
import pandas as pd

# Function to load data
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path, sep=';')
    return data

# Streamlit app layout
st.title('CSV Data Viewer')

st.write('This app loads and displays data from a CSV file on Google Drive.')

file_path = st.text_input('Enter the file path:', '/content/drive/My Drive/Avito_Dataset old.csv')

if file_path:
    try:
        data_cleaned = load_data(file_path)
        st.write(data_cleaned.head())
    except Exception as e:
        st.error(f"Error loading data: {e}")
