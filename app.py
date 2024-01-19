import streamlit as st
st.title("Find the Maximum Number among three")
first_num = st.number_input("Enter the first numebr")
second_num = st.number_input("Enter the second number")
third_num = st.number_input("Enter the third number")

name_button = st.button("Submit")
if name_button:
    max_number = max(first_num, second_num, third_num)
    st.success(f"The maximum number is: {max_number}")