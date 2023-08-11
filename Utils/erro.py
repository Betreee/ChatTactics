# ####
# # In this ErrorHandler class we have methods:

# handle_error: It logs the error and decides whether to notify the user or not based on the error type.
# notify_user: It sends a notification to the user.
# recover_from_error: Attempts to recover from an error and handles any new errors that may occur during recovery.
# The class collaborates with the Logger class from the previous example to log messages as needed. For simplicity, user notifications are just printed to the console in this example. In a real-world scenario, these could be emails, pop-up messages, etc. depending on your application's requirements.  #
# ####
from .logg  import Logger as logger
class ErrorHandler:
    def __init__(self, logger=logger):
        self.logger = logger

    def handle_error(self, error):
        self.logger.log_error(error)

        # Depending on the error, decide whether to notify the user or not.
        if isinstance(error, Exception):  
            self.notify_user("An error has occurred: {}".format(error))

    def notify_user(self, notification):
        print("NOTIFICATION: {}".format(notification))

    def recover_from_error(self, error):
        try:
            # Attempt recovery from error here...
            pass
        except Exception as e:
            self.handle_error("Recovery attempt failed: {}".format(e))
