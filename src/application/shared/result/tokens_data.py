from dataclasses import dataclass


@dataclass
class TokensData(object):
    access_token: str
    refresh_token: str
