import streamlit as st
from UserManagement import  Atho
from DataManagement.ondisk import DataStorage as ds
from UserManagement import User
# from DataManagement.database import database
from DataManagement.database import Repository
@Atho.Authenticators.with_authorization
def registration_page():
    # Collecting user information
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit = st.form_submit_button(label="Register")

    if submit:
        if password == confirm_password:

            ds.save_user_data(username, email, password)
            st.success(f"Welcome {username}, you have been successfully registered!")
        else:
            st.error("Invalid credentials")
    else:
        st.error("Passwords do not match")
        
    def register_user(username, email, password):
        existing_user = User.get_user_by_username(username)
        if existing_user:
            print(f"Username {username} already exists! Please choose a different username.")
            return False
        user = User(username=username, email=email, password=password)
        Repository.add_user(user)
        print(f"User {username} registered successfully!")
        return True