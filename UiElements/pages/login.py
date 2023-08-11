import streamlit as st
from UserManagement.Atho import with_authorization
@with_authorization
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
        if username == "admin" and password == "admin":
            st.success("Logged In as {}".format(username))
            # You can add more content for the logged-in user here
        else:
            st.warning("Incorrect Username/Password")
main()
