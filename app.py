# st.title
# st.text_input
# st.number_input
# st.selectbox

import streamlit as st

st.title("Welcome to my App")
st.write("This is a simple Streamlit application.")

name = st.text_input("Enter your name", "Guest")
st.write(f"Hello, {name}!")

if st.button("Click Me"):
    st.balloons()
    st.success("Button clicked!")
