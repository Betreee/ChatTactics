import streamlit as st
from DataManagement.ondisk import DataStorage
from DataManagement.database import User, Repository
USER = User

def registration_page(): 
    # Collecting user information
    col1 , col2 = st.columns(2)
    with col1:
        "---"
        st.markdown("# Register")
        st.markdown("## Enter your details OVER here -->")
        st.markdown("---")
    with col2:
        with st.form(key="register_form"):
            st.markdown("### Username")
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit = st.form_submit_button(label="Register")
            if submit:
                if password == confirm_password:
                    try:
                        user = User(username=username, email=email, password=password)
                        st.success(f"Welcome {username}, you have been successfully registered!")
                        # You can add code here to save the registration info, e.g., in a database
                    except ValueError as e:
                        st.error(str(e))

    
    on_success = st.empty()
    on_failure = st.empty()    


        
def reg(key, USER ):
    if key != None:
        # gen a key
        key = DataStorage.new_key()
        # encrypt and save data
        crypt = DataStorage(key)
        DataStorage.save_key(key)
        crypt.save_data("user_file.txt",data = USER)
        st.success("Registration successful!")
        Repository.add_user(USER)
        st.success("Registration successful!")
        st.balloons()
        ###! todo email client and verify human
    else:
        st.error("Registration failed!")
        st.write("it seems you already have keys for this ride!")
registration_page()
        
       



    
