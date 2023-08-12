import uuid


class SessionStore:
    def __init__(self):
        self.sessions = {}
        self.tokens = {}
        self.history = {}

    def create_session_id(self) -> str:
        """Generates a new session id."""
        return str(uuid.uuid4())

    def store_session_data(self, session_id: str, session: 'Session'):
        """Stores the session data associated with the given session id."""
        self.sessions[session_id] = session
        self.tokens[session_id] = session.user.token
        if session_id not in self.history:
            self.history[session_id] = []
        self.history[session_id].append(session.session_data)

    def get_session_data(self, session_id: str) -> 'Session':
        """Retrieves the session data associated with the given session id."""
        return self.sessions.get(session_id)

    def delete_session_data(self, session_id: str):
        """Deletes the session data associated with the given session id."""
        self.sessions.pop(session_id, None)
        self.tokens.pop(session_id, None)
        self.history.pop(session_id, None)

    def delete_all_session_data(self):
        """Deletes all session data."""
        self.sessions = {}
        self.tokens = {}
        self.history = {}
        
class Session:
    def __init__(self, session_id, user, session_data, preferences=None):
        self.session_id = session_id
        self.user = user
        self.session_data = session_data
        self.preferences = preferences or {
            'language': 'en',
            'theme': 'light',
            'timezone': 'UTC',
            'currency': 'USD',
            'country': 'US',
            'currency_symbol': '$',
            'currency_symbol_position': 'before',
            'currency_decimal_separator': '.',
            'currency_thousands_separator': ',',
            'currency_precision': 2,
            'currency_code': 'USD',
        }

    def get_user(self):
        return self.user

    def get_session_data(self):
        return self.session_data

    def get_token(self):
        return self.user.token
    def get_preferences(self):
        return self.preferences

    def get_session_id(self):
        return self.session_id

class SessionManager:
    def __init__(self, session_store: SessionStore):
        self.session_store = session_store

    def create_session(self, user, session_data, preferences=None) -> Session:
        session_id = self.session_store.create_session_id()
        session = Session(session_id, user, session_data, preferences)
        self.session_store.store_session_data(session_id, session)
        return session

    def get_session(self, session_id: str) -> Session:
        session = self.session_store.get_session_data(session_id)
        return session

    def delete_session(self, session_id: str):
        self.session_store.delete_session_data(session_id)

    def delete_all_sessions(self):
        self.session_store.delete_all_session_data()

    def update_preferences(self, session_id: str, preferences: dict):
        session = self.get_session(session_id)
        if session:
            session.preferences = preferences
            self.session_store.store_session_data(session_id, session)
