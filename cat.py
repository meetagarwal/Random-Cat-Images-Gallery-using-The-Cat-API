import streamlit as st
import requests


API_KEY = "live_FVhVQYFXyHabAEN2g9w8mSWPq0oauobRlHoSLfGUvyDMilUuXkbn5o22ZRD04cfT"

def get_breeds():
    url = "https://api.thecatapi.com/v1/breeds"
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

def get_cat_images(breed_id=None, limit=9):
    url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&size=small"
    if breed_id:
        url += f"&breed_ids={breed_id}"
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []


st.title("🐱 Random Cat Gallery")


breeds = get_breeds()
breed_options = {breed['name']: breed['id'] for breed in breeds}
selected_breed = st.selectbox("Select Breed:", ["All"] + list(breed_options.keys()))

if st.button("Load Cats 🐾"):
    breed_id = breed_options[selected_breed] if selected_breed != "All" else None
    cat_images = get_cat_images(breed_id)
    
    
    cols = st.columns(3)
    for i, cat in enumerate(cat_images):
        with cols[i % 3]:
            st.image(cat['url'], use_column_width=True)


