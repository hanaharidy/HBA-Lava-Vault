from cryptography.fernet import Fernet
import json
from password_generator import LavaLampGenerator

class VaultManager:
    def __init__(self, key_file="secret.key", vault_file="vault.json"):
        self.key_file = key_file
        self.vault_file = vault_file
        self.key = self._load_or_create_key()
        self.cipher = Fernet(self.key)
        self.vault = self._load_vault()
        self.generator = LavaLampGenerator()

    def _load_or_create_key(self):
        try:
            with open(self.key_file, "rb") as f:
                return f.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key

    def _load_vault(self):
        try:
            with open(self.vault_file, "r") as f:
                encrypted_data = json.load(f)
                return self._decrypt_vault(encrypted_data)
        except FileNotFoundError:
            return {}

    def _decrypt_vault(self, encrypted_data):
        decrypted = self.cipher.decrypt(encrypted_data.encode()).decode()
        return json.loads(decrypted)

    def save_vault(self):
        encrypted = self.cipher.encrypt(json.dumps(self.vault).encode()).decode()
        with open(self.vault_file, "w") as f:
            json.dump(encrypted, f)

    def add_password(self, service, username, password):
        self.vault[service] = {"username": username, "password": password}
        self.save_vault()

    def generate_password(self):
        return self.generator.generate()
    