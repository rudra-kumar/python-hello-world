from enum import Enum


class Token:

    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def to_string(self):
        return str(self.token_type) + " " + str(self.value)


class TokenType(Enum):
    KEYWORD = 1,
    NUMERIC = 2,
    EOF = 3
