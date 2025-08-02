import bcrypt

from src.core.utils import PasswordEncoder


class BcryptPasswordEncoder(PasswordEncoder):
    def encode(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed.decode('utf-8')

    def is_matched(self, value: str, encoded: str) -> bool:
        return bcrypt.checkpw(value.encode('utf-8'), encoded.encode('utf-8'))
