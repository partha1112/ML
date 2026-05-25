import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/classify"

st.title("Sentiment Analysis Client")
st.write("Enter a movie review and call the FastAPI sentiment endpoint.")

review = st.text_area("Review", "The movie not bad. I was excited")

if st.button("Analyze Sentiment"):
    if not review.strip():
        st.warning("Please enter a review before sending.")
    else:
        params = {"review": review}
        try:
            response = requests.get(API_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            st.success("API call successful")
            st.json(data)
        except requests.exceptions.RequestException as err:
            st.error(f"Request failed: {err}")
        except ValueError:
            st.error("Invalid response from API. Expected JSON.")
