import jwt
import streamlit as st
from UserManagement.Atho import authorize_request
from Utils.erro import ErrorHandler
class Authenticator:
    
    def authenticate(self, username, password):
        # Implementation to authenticate user
        # Returns True or False
        pass
    def validate_credentials(self, username, password):
        # Implementation to validate user credentials
        # Returns True or False
        pass
    def manage_tokens(self, user):
        # Implementation to generate and manage authentication tokens
        pass
    

    def with_authorization(page_func):
        def wrapper(*args, **kwargs):
            token = st.session_state.get('token')
            if not authorize_request(token):
                st.error("Unauthorized")
                return
            return page_func(*args, **kwargs)
        return wrapper
    import jwt

    def authorize_request(token):
        try:
            payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
            # Verify user_id and token expiration
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False 
        except Exception as e:
            ErrorHandler.handle_error(e)