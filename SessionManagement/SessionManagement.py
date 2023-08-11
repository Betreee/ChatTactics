class SessionStore(object):
    def __init__(self):
        self.sessions = {}

    def create_session_id(self):
        # Generates a new session id
        pass

    def store_session_data(self, session_id, session):
        # Stores the session data associated with the given session id
        self.sessions[session_id] = session

    def get_session_data(self, session_id):
        # Retrieves the session data associated with the given session id
        return self.sessions.get(session_id)

    def delete_session_data(self, session_id):
        # Deletes the session data associated with the given session id
        if session_id in self.sessions:
            del self.sessions[session_id]

    def delete_all_session_data(self):
        # Deletes all session data
        self.sessions = {}
        
class Session(object):  
    def __init__(self, session_id, user, session_data):
        self.session_id = session_id
        self.user = user
        self.session_data = session_data
        self.preferences = {}
        self.preferences['language'] = 'en'
        self.preferences['theme'] = 'light'
        self.preferences['timezone'] = 'UTC'
        self.preferences['currency'] = 'USD'
        self.preferences['country'] = 'US'
        self.preferences['currency_symbol'] = '$'
        self.preferences['currency_symbol_position'] = 'before'
        self.preferences['currency_decimal_separator'] = '.'
        self.preferences['currency_thousands_separator'] = ','
        self.preferences['currency_precision'] = 2
        self.preferences['currency_code'] = 'USD'
        

    def get_user(self):
        return self.user
    def get_session_data(self):
        return self.session_data

class SessionManager(object):
    def __init__(self, session_store:SessionStore):
        self.session_store = session_store
    def create_session(self, user, session_data):
        session_id = self.session_store.create_session_id()
        session = Session(session_id, user, session_data)
        self.session_store.store_session_data(session_id, session)
        return session
    def get_session(self, session_id):
        session = self.session_store.get_session_data(session_id)
        if session is None:
            return None
        return session
    def delete_session(self, session_id):
        self.session_store.delete_session_data(session_id)
    def delete_all_sessions(self):
        self.session_store.delete_all_session_data()
    def update_preferences(self, session_id, preferences):
        session:Session = self.get_session(session_id)
        if session is None:
            return None
        session.preferences = preferences
        self.session_store.store_session_data