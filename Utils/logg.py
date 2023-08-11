import logging
import os
import shutil
from datetime import datetime
#This Logger class has methods to:

# create_log_dir: Create a directory for logs if it doesn't exist.
# log_message: Log a message at a certain level (info, warning, error).
# log_error: Specifically log an error message.
# create_log_file: Create a new log file.
# archive_logs: Move old logs to an archive directory and create a new log file.
# This logger can be used in other classes to log messages as needed. The archive_logs method could be called periodically to clean up the log directory.#
# 
# 
# #?To use the `Logger` class, you need to follow these steps:
'''
# 1. Import the necessary modules:
#    ```python
#    import logging
#    import os
#    import shutil
#    from datetime import datetime
#    ```

# 2. Create an instance of the `Logger` class:
#    ```python
#    logger = Logger()
#    ```
#    This will create a new instance of the `Logger` class with default log and archive directories.

# 3. Log messages using the `log_message` method:
#    ```python
#    logger.log_message("This is an informational message", "info")
#    logger.log_message("This is a warning message", "warning")
#    logger.log_message("This is an error message", "error")
#    ```
#    The `log_message` method takes two parameters: the log message and the log level (which can be "info", "warning", or "error"). It will log the message with the specified level using the `logging` module.

# 4. Log errors using the `log_error` method:
#    ```python
#    try:
#        # Code that may raise an exception
#    except Exception as e:
#        logger.log_error(e)
#    ```
#    The `log_error` method takes an `error` parameter and logs an error message using the `logging.error` function. It's commonly used within exception handling blocks to log any raised exceptions.

# 5. Archive log files:
#    ```python
#    logger.archive_logs()
#    ```
#    The `archive_logs` method archives the current log file by moving it to the specified `archive_dir`, appending a timestamp to the filename. It then creates a new empty log file using the `create_log_file` method.

# By following these steps, you can effectively log messages and manage log files using the `Logger` class. Remember to customize the log and archive directories according to your requirements.
# 
# '''


class Logger:
    def __init__(self, log_dir='./logs', archive_dir='./archive'):
        self.log_dir = log_dir
        self.archive_dir = archive_dir
        self.create_log_dir()

        logging.basicConfig(filename=os.path.join(self.log_dir, 'app.log'), level=logging.DEBUG)
    
    def create_log_dir(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def log_message(self, message, level):
        if level.lower() == 'info':
            logging.info(message)
        elif level.lower() == 'warning':
            logging.warning(message)
        elif level.lower() == 'error':
            logging.error(message)
    
    def log_error(self, error):
        logging.error("Error: {}".format(error))

    def create_log_file(self):
        with open(os.path.join(self.log_dir, 'app.log'), 'w'):
            pass
    
    def archive_logs(self):
        if not os.path.exists(self.archive_dir):
            os.makedirs(self.archive_dir)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        shutil.move(os.path.join(self.log_dir, 'app.log'), 
                    os.path.join(self.archive_dir, 'app_{}.log'.format(timestamp)))

        self.create_log_file()