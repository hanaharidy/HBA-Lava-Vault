import random

class LavaLampGenerator:
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        
    def generate(self, length=12):
        return ''.join(random.SystemRandom().choices(self.characters, k=length))