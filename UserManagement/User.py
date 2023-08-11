#User.py

import jwt
from SessionManagement.SessionManagement import SessionManager, SessionStore
from UserManagement.Atho import Authenticator


session_store = SessionStore()
session_manager = SessionManager(session_store)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username    


class UserManager:
    def __init__(self):
        self.session_manager:SessionManager = SessionManager(session_store)
        self.authenticator = Authenticator()
    def get_user_by_username(self, username):
        # Query the user store (e.g., database) for a user with the given username
        user = user_store.get(username)
        return user

    def generate_token(username):
        payload = {
            'username': username,
            # Add other claims as needed
        }
        token = jwt.encode(payload, 'secret_key', algorithm='HS256')
        return token
    def login(self, username, password):
        user = self.get_user_by_username(username)
        if user and user.password == password:
            token = self.generate_token(username)
            return True, token
        return False, None
    def logout(self):
        self.session_manager.delete_session()

    def updatePreferences(self, preferences):
        self.session_manager.update_preferences(preferences)
        


user_manager = UserManager()
success, token = user_manager.login('valid_username', 'valid_password')
assert success == True
assert token is not None

success, token = user_manager.login('invalid_username', 'invalid_password')
assert success == False
assert token is None
