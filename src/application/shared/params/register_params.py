from dataclasses import dataclass


@dataclass
class RegisterParams:
    email: str
    password: str