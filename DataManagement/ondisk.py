import json
import os
from cryptography.fernet import Fernet

class SecureFileEnDeCryptor:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    @staticmethod
    def new_key():
        return Fernet.generate_key()
         
    def save_encrypted_data(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.fernet.encrypt(file_data)
    
    def load_decrypted_data(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        decrypted_data = self.fernet.decrypt(file_data)
    
    
class DataStorage:
    def __init__(self):
        self.Secure = SecureFileEnDeCryptor

        
    def save_data(self, filename, data):
        with open(filename, 'wb') as file:
            file.write(data)
            return file

    def read_data(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                file = file.read()
            return file
        else:
            return None

    def delete_file(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def destroy_data(self, filenames):
        for filename in filenames:
            self.delete_file(filename)
            return "destroyed"
def save_user_data(username, email, password):
    key = DataStorage.new_key()
    crypt = DataStorage(key)
    DataStorage.save_key(key)
    user_data = {"username": username, "email": email, "password": password}
    crypt.save_data("user_file.txt", data=json.dumps(user_data))
# key = DataStorage.new_key() # generate new key
# storage = DataStorage(key)
# storage.save_key() # save key
# key = storage.load_key() # load key

# # Save data
# filename = 'data.txt'
# data = 'This is some sensitive information'
# enc = storage.save_data(filename, data)
# print(open(filename, 'rb').read())
# # Read data
# read_data = storage.read_data(filename)
# print(read_data)  # Output: This is some sensitive information

# # Delete file
