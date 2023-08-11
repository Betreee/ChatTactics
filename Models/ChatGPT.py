from typing import Callable,Any
import openai
import streamlit as st
from Utils.logg import Logger
logger = Logger(__name__)
from Utils.erro import ErrorHandler
err = ErrorHandler(logger)                                                                                                              




class ChatGPT:
    def send_message(self, message: str,analyzer_name:str,role:str,  callback: Callable) -> Any:
        # Send the message to Chat GPT
        openai.api_key = st.secrets("OPENAI_API_KEY")
        message = [{"role": role, "text": message}]
        try:

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message,  # run create messages and create a var while doing that and pass those to this function as the first parm
                temperature=0.6,
                stream=True,  # this time, we set stream=True
            )

            role = ""
            test = ""

            for chunk in response:
                role += chunk["choices"][0].delta.get("role", "")
                test += chunk["choices"][0].delta.get("content", "")
                self.data["result"] = {analyzer_name, test}
            #receive
            response = self.receive_message(message)
            # Route the response to the appropriate location
            self.route_message(response, callback)
            return response
        except Exception as e:
                err.handle_error(e)

            
    def receive_message(self, message: str) -> Any:
        # Implementation to receive the response from Chat GPT
        # Possibly store or process the response
        pass

    def route_message(self, response: Any,  callback: Callable) -> None:
        # Determine the correct destination for the response
        # Send it to the appropriate location (e.g., callback, analyzer, UI)
        pass
