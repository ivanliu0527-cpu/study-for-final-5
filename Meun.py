import streamlit as st 
from streamlit_option_menu import option_menu

st.title("Hello student")
st.write("This is your Python Programming course")

with st.sidebar:
  selected = option_meun(
    options = ["Home", "About", " Contact"],
    icon = ["1-circle-fill",
            "2-circle-fill",
            "3-circle-fill"],
    meun_icon = "emoji-smle-fill",
    default_index=0,
  )

if selected == "Home":
  st.title(f"Welcome to the {selected} page.")
if selected == "About":
  st.title(f"Welcome to the {selected} page.")
if selected == "Contact":
  st.title(f"Welcome to the {selected} page.")
