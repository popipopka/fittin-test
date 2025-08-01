from dataclasses import dataclass


@dataclass
class LoginParams:
    email: str
    password: str