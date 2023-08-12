import streamlit as st
from UserManagement.Atho import Authenticators
@Authenticators.with_authorization
def main():
    st.title("Login")
    st.subheader("Login Section")
    
    
    username = st.text_input("User Name",)
    # st.write(username)
    password = st.text_input("Password", type='password')
    #st.write(password)    
    # st.write("Username: {}".format(username))
    # st.write("Password: {}".format(password))
    st.write("")
    if st.button("Login"):
        st.title("Welcome")
        st.write("Welcome {}".format(username))
        st.write("You are logged in")
        st.write("")
        st.write("")
        st.write("")                    
        
    else:
        st.warning("Incorrect Username/Password")
main()
