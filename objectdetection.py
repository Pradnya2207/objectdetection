import requests
import streamlit

API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# output = query("C:\\Users\\Sanika\\Downloads\\parrot.jpg")
# print(output)

###########################

import streamlit as st
from pathlib import Path
import requests

st.title("Demo")
# st.image(res, width=800)
st.markdown("**Please Upload the file :**")
uploaded_file = st.file_uploader(label = "Upload file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file)
with st.form(key ="Form:", clear_on_submit= True):
    # Name = st.text_input("Name:")
    # Email = st.text_input("Email Id :")
    Submit = st.form_submit_button(label = 'Submit')
if Submit:
    save_folder = 'D:/FDP'
    save_path = Path(save_folder, uploaded_file.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())

    if save_path.exists():
        st.success(f'File {uploaded_file.name} is successfully saved!')
    st.markdown("**The file is successfully uploaded.**")

    # Save uploaded file to 'F:/tmp' folder
    output = query("D:\\FDP\\"+uploaded_file.name)
    st.snow()
    st.success(output)
