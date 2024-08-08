import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io

# Set up Google Drive API
def get_gdrive_service():
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    service = build('drive', 'v3', credentials=credentials)
    return service

# Function to download file from Google Drive
def download_file_from_gdrive(service, file_id):
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    file.seek(0)
    return file

# Streamlit app layout
st.title('CSV Data Viewer from Google Drive')

st.write('This app loads and displays data from a CSV file on Google Drive.')

# Google Drive file ID
file_id = st.text_input('Enter the Google Drive file ID:', 'your_file_id_here')

if file_id:
    try:
        service = get_gdrive_service()
        file = download_file_from_gdrive(service, file_id)
        data_cleaned = pd.read_csv(file, sep=';')
        st.write(data_cleaned.head())
    except Exception as e:
        st.error(f"Error loading data: {e}")
