# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st

model = pickle.load(open("C:/Users/anshu/Desktop/AI-ML Course/Project/pkl Files/final_model.pkl","rb"))
cv = pickle.load(open("C:/Users/anshu/Desktop/AI-ML Course/Project/pkl Files/count_vectorizer.pkl","rb"))

def main():
    st.title("SQL Injection Query Detection")
    st.subheader("Application to Detect whether entered Query is mallicious or Non-Mallicious")
    msg = st.text_input("Enter Test Query: ")
    
    if st.button("Predict"):
        data = [msg]
        vect=cv.transform(data).toarray()
        prediction=model.predict(vect)
        result = prediction[0]
        
        if result == 1:
            st.error("Mallicious Query")
        else:
            st.success("Non-Mallicious Query")
        
        
main()
