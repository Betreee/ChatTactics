#User.py

from SessionManagement.SessionManagement import SessionManager
from UserManagement.Atho import Authenticator


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username    


class UserManager:
    def __init__(self):
        self.session_manager:SessionManager = SessionManager()
        self.authenticator = Authenticator()

    def login(self, username, password):
        if self.authenticator.authenticate(username, password):
            self.session_manager.start_session(username)
            return True
        else:
            return False

    def logout(self):
        self.session_manager.delete_session()

    def updatePreferences(self, preferences):
        self.session_manager.update_preferences(preferences)