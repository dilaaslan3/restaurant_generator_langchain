import streamlit as st
import llm_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine" , ("Italian", "Turkish", "Mexican", "American"))


if cuisine:
    response = llm_helper.generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)