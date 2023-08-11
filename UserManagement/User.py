# User.py
"""The User class is missing the _usernames attribute that is used in the get_user_by_username function. 
The login function should also check if the user exists before attempting to generate a token. The assert
statements in the code should be replaced with more appropriate tests. The logout function does not accept
any parameters, so it is unclear how it is supposed to delete a session. The updatePreferences function 
should accept a parameter for the user's preferences. The add_user function in the Repository class should 
also accept a password parameter..,bn"""
import uuid
import jwt
from SessionManagement.SessionManagement import SessionManager, SessionStore
from UserManagement.Atho import Authenticators 

session_store = SessionStore()

session_manager = SessionManager(session_store)


class User:
    _usernames = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __str__(self):
        return self.username


class UserManager:
    def __init__(self):
        self.session_manager: SessionManager = SessionManager(session_store)
        self.authenticator = Authenticators.authorize_request

    def get_user_by_username(self, username):
        for user in User._usernames:
            if User._usernames == username:
                return user
        return None

    def generate_token(username):
        payload = {
            "username": username,
            # Add other claims as needed
        }
        token = jwt.encode(payload, "secret_key", algorithm="HS256")
        return token

    @Authenticators.with_authorization
    def login(self, username, password):
        user = self.get_user_by_username(username)
        if user and user.password == password:
            token = self.generate_token(username)
            return True, token
        return False, "Forgot password? or Get to become one of Us! register now!"

    def logout(self):
        self.session_manager.delete_session()

    def updatePreferences(self, preferences):
        self.session_manager.update_preferences(preferences)


from DataManagement.database import User, Repository

repository = Repository()

user = User(username=f"{uuid.uuid4()}", email="email", password="password")
repository.add_user(user)
user_manager = UserManager()
use = User(
    username=f"{uuid.uuid4()}", password="valid_password", email="valid@email.com"
)
# add to repo
repository.add_user(use)
if use in repository.get_users():
    print("User exists")
else:
    print("User does not exist")

success, token = user_manager.login( uuid.uuid4(),"valid_password")
print(success)
assert success == True
assert token is not None

success, token = user_manager.login(uuid.uuid5(), "invalid_password")
print(success)
assert success == False
assert token is None
