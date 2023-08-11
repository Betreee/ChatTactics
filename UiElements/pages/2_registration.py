import streamlit as st
from UserManagement.Atho import with_authorization
from DataManagement.ondisk import save_user_data
@with_authorization
def registration_page():
    # Collecting user information
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit = st.form_submit_button(label="Register")

    if submit:
        if password == confirm_password:

            save_user_data(username, email, password)
            st.success(f"Welcome {username}, you have been successfully registered!")
        else:
            st.error("Invalid credentials")
    else:
        st.error("Passwords do not match")