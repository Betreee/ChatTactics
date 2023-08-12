# User.py
"""The User class is missing the _usernames attribute that is used in the get_user_by_username function. 
The login function should also check if the user exists before attempting to generate a token. The assert
statements in the code should be replaced with more appropriate tests. The logout function does not accept
any parameters, so it is unclear how it is supposed to delete a session. The updatePreferences function 
should accept a parameter for the user's preferences. The add_user function in the Repository class should 
also accept a password parameter..,bn"""
import os
import uuid
import jwt
from DataManagement.database import Repository
from SessionManagement.SessionManagement import SessionManager, SessionStore
from UserManagement.Atho import Authenticators 
SecKey = os.getenv('SECRET_KEY')
session_store = SessionStore()

session_manager = SessionManager(session_store)


class User:
    _usernames = []
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email
        
    def __str__(self):
        return self.username


class UserManager:
    def __init__(self):
        self.session_manager: SessionManager = SessionManager(session_store)
        self.authenticator = Authenticators.authorize_request
        self.repository = Repository()
        
        
    def register_user(self, user:User):
        if self.get_user_by_username(user.username) is None:
            self.repository.add_user(user)
            User._usernames.append(user.username)
            return True
        return False
    
    def get_user_by_username(self, username):
        for user in User._usernames:
            if username == user:
                return user
        return None

    def generate_token(username):
        payload = {
            "username": username,
            # Add other claims as needed
        }
        token = jwt.encode(payload, SecKey, algorithm="HS256")
        return token

    def get_user_by_username(self, username):
        for user in Repository.get_users():
            if username == user:
                return user
        return None

    def login(self, username, password):
        user:User = self.get_user_by_username(username)
        if user and user.password == password:
            token = self.generate_token(username)
            session_data = {"expire": "1 day", "user": user, "token": token}
            session = self.session_manager.create_session(user, session_data)
            return (True, token)
        return (False, "Invalid")

    def logout(self, token):
        # Logic to find the session ID by token
        sessionId = None
        for session_id, session in self.session_manager.get_all_sessions().items():
            if session['token'] == token:
                sessionId = session_id
                break
        
        if sessionId:
            self.session_manager.delete_session(sessionId)


    def updatePreferences(self, sessionId, preferences):
        self.session_manager.update_preferences(sessionId, preferences)

print("______________________test____________________")
def test():
    from DataManagement.database import User, Repository

    repository = Repository()
    user = User(username=f"{uuid.uuid4()}", email="email", password="password")
    repository.add_user(user)
    user_manager:UserManager = UserManager()
    # register user
    
    use = User(
        username=f"benny", password="valid_password", email="valid@email.com"
    )
    # log in
    session = user_manager.login(use)
    print(session)
    
    # log out
    user_manager.logout(session)
    print(session)

    # add to repo
    
    repository.add_user(use)
    if use in repository.get_users():
        print("User exists")
    else:
        print("User does not exist")
    
    createdSession = user_manager.session_manager.create_session(use)
    session = user_manager.session_manager.get_session()
    if session:
        print("Session exists",)
    else:
        print("Session does not exist")
    
        
test()
