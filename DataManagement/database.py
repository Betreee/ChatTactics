# save delete read get destroy data integrity from dataclasses import dataclass

from dataclasses import dataclass

from Utils.erro import ErrorHandler  
@dataclass
class ChatHistory:
    messages: list
    participants: list
    timestamp: int

@dataclass
class User:
    username: str
    email: str
    password: str
    
    _usernames = set()  # Class-level set to keep track of usernames

    def __post_init__(self):
        try:
            if self.username  not in User._usernames:
                User._usernames.add(self.username)
        except Exception as e:
            
            ErrorHandler().recover_from_error(ValueError(f"Username {self.username} is already taken."))
                      

            
    

@dataclass
class AnalysisResults:
    sentiment_analysis: dict
    topics_discussed: list
    keywords: list

class Repository:
    def __init__(self):
        self.chat_history = []
        self.users = []
        self.analysis_results = {}
    
    def add_chat_history(self, chat_history):
        self.chat_history.append(chat_history)
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_analysis_result(self,name, analysis_result):
        self.analysis_results[name] = analysis_result
    
    def get_chat_history(self):
        return self.chat_history
    
    def get_users(self):
        return self.users
    
    def get_analysis_results(self):
        return self.analysis_results