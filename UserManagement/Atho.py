import jwt
import streamlit as st

from Utils.erro import ErrorHandler
class Authenticators:
    def with_authorization(page_func):
        def wrapper(*args, **kwargs):
            token = st.session_state.get('token')
            if not Authenticators.authorize_request(token):
                st.error("Unauthorized")
                return
            return page_func(*args, **kwargs)
        return wrapper


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
            
