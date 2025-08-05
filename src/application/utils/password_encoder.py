from abc import ABC

import bcrypt


class PasswordEncoder(ABC):
    def encode(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def is_matched(self, value: str, encoded: str) -> bool:
        return bcrypt.checkpw(value.encode('utf-8'), encoded.encode('utf-8'))