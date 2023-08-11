import streamlit as st
from PIL import Image 
import sys
sys.path.append('C:\\Users\\be\\OneDrive\\Documents\\GitHub\\chattactics\\UserManagement')
sys.path.append('C:\\Users\\be\\OneDrive\\Documents\\GitHub\\chattactics\\DataManagement')                                                                                                                                                                                                                                                                                              
img = Image.open('UiElements\static\logo3.png')
# st.image(, width=100)

@st.cache_resource()
def splash_screen():
    st.title("Welcome to My Communications App!")
    st.image(img, use_column_width=True) # You can add your logo here
    st.subheader("Connecting People Across the Globe")
    st.write("Your one-stop solution for seamless communication, collaboration, and connection.")
    st.write("Click the button below to get started.")
splash_screen()
if st.button("Start"):
    st.success("Let's dive in!")                                                                    

        # You can navigate to the main app or another page here

# Call the splash_screen function to display the splash screen