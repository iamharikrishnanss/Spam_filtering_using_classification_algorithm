import pickle
import streamlit as st

model = pickle.load(open("spam.pkl","rb"))
cv = pickle.load(open("vectorizer.pkl","rb"))

st.title("Email spam Classification")
email = st.text_input("Enter the text : ")
if st.button("Predict"):
    data = [email]
    vector = cv.transform(data).toarray()
    result = model.predict(vector)
    if result[0] == 1:
        st.error("This is a spam mail")
    else:
        st.success("this is not a spam mail")