#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]

import openai
import os

def generate_code(input_string): 
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt= input_string +"\n",
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer

# Define the Streamlit app
def app():
    st.header("Welcome to CodeGPT")
    st.subheader("Louie F. Cervantes M. Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("CodeGPT will generate program codes from natural language instructions")
    st.write("One on the most useful uses of generative AI is to generate programming codes in several languages.  A very useful tool that would speed up and enhance the output of software developers.")
    st.write("Copy paste one of the following task into the input box.  You can also come up with you own set of instructions.")
    st.write("Write a program that calculates the average of a list of numbers.")
    st.write("Create a function that reverses a string.")
    st.write("Write a program that takes in two numbers and outputs their sum.")
    st.write("Create a function that checks if a string is a palindrome.")
    st.write("Write a program that reads in a file and outputs the number of lines in the file.")
    st.write("Create a function that takes in a list of integers and returns the largest integer in the list.")
    st.write("Write a program that generates a random number between 1 and 100.")
    st.write("Create a function that takes in a string and returns the number of vowels in the string.")
    st.write("Write a program that reads in a list of words and outputs the number of words that start with the letter 'a'.")
    st.write("Create a function that takes in a list of strings and returns the string with the most characters.")
    
    language = 'python'
    options = ['python', 'Java', 'C++']
    selected_option = st.selectbox('Select the programming language', options)
    if selected_option=='python':
        language = selected_option
    if selected_option=='Java':
        language = selected_option
    if selected_option=='C++':
         language = selected_option
             
    # Create a multiline text field
    user_input = st.text_area('Paste the instructions in this box', height=10)
    
             
    # Display the text when the user submits the form
    if st.button('Submit'):
        output = generate_code("Generate program codes in the language " + language + " to perform the task " + user_input)
        st.write(output)

# Run the app
if __name__ == "__main__":
    app()
