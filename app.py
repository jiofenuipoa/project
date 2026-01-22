# st.title
# st.text_input
# st.number_input
# st.selectbox

import streamlit as st

# Basic layout components
st.title("Welcome to my App")
st.write("This is a simple Streamlit application.")

# Adding a simple interactive widget
name = st.text_input("Enter your name", "Guest")
st.write(f"Hello, {name}!")

if st.button("Click Me"):
    st.balloons()
    st.success("Button clicked!")
