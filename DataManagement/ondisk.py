import os
from cryptography.fernet import Fernet


class DataStorage:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    @staticmethod
    def new_key():
        return Fernet.generate_key()

    def save_key(self):
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        if os.path.isfile('key.key'):
            return open('key.key', 'rb').read()
        else:
            raise Exception('Key not found')

    def encrypt(self, data):
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = self.fernet.decrypt(encrypted_data).decode()
        return decrypted_data

    def save_data(self, filename, data):
        encrypted_data = self.encrypt(data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def read_data(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                encrypted_data = file.read()
            data = self.decrypt(encrypted_data)
            return data
        else:
            return None

    def delete_file(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def destroy_data(self, filenames):
        for filename in filenames:
            self.delete_file(filename)

key = DataStorage.new_key() # generate new key
storage = DataStorage(key)
storage.save_key() # save key
key = storage.load_key() # load key

# Save data
filename = 'data.txt'
data = 'This is some sensitive information'
enc = storage.save_data(filename, data)
print(open(filename, 'rb').read())
# Read data
read_data = storage.read_data(filename)
print(read_data)  # Output: This is some sensitive information

# Delete file
