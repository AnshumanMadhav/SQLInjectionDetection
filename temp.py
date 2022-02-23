# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st

model = pickle.load(open("model.pkl","rb"))
cv = pickle.load(open("count_vectorizer.pkl","rb"))

def main():
    st.title("SQL Injection Query Detection")
    st.subheader("Build with Streamlit and Python")
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

    


    
    

 
