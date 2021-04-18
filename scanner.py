from tokens import Token
from tokens import TokenType

"""
What data does a scanner represent - It will take the source code and convert it into tokens
1. It has the source
2. It has a list of tokens 
How do we scan through the source code
We take it one step at a time
We go character by character 
So we need to store some state
    Current - the currect Character the state is in 
Our scanner will go over the string one by one
So we need some methods to advance the scanner 
A way to consume a character
A way to check if the character is the last one 
"""


class Scanner:
    KEYWORDS = ['P', 'D', 'W', 'N', 'E', 'S', 'U']

    def __init__(self, source):
        self.source = source
        self.currentIndex = 0
        self.tokens = []

    def scan(self):
        while not self.is_eof():
            currentCharacter = self.consume()
            if currentCharacter == ' ' or currentCharacter == '\n':
                continue
            elif currentCharacter.isalpha():
                self.process_alpha(currentCharacter)
            elif currentCharacter.isdigit():
                self.process_digit(currentCharacter)
            else:
                raise Exception(f"Invalid character {currentCharacter}")

        self.add_token(TokenType.EOF, None)
        return self.tokens

    def advance(self):
        self.currentIndex = self.currentIndex + 1

    def add_token(self, token):
        self.tokens.append(token)

    def add_token(self, token_type, token_value):
        self.tokens.append(Token(token_type, token_value))

    def consume(self):
        self.advance()
        return self.source[self.currentIndex - 1]

    def current(self):
        return self.source[self.currentIndex]

    def peek(self):
        return self.source[self.currentIndex + 1]

    def is_eof(self):
        if self.currentIndex >= len(self.source):
            return True
        return False

    def process_alpha(self, starting_alpha):
        alphabet = starting_alpha
        while not self.is_eof() and (self.current().isdigit() or self.current().isalpha()):
            alphabet += self.consume()
        if alphabet in Scanner.KEYWORDS:
            self.add_token(TokenType.KEYWORD, alphabet)
        else:
            raise Exception(f"Keyword {alphabet} not supported")

    def process_digit(self, first_digit):
        digit = first_digit
        while not self.is_eof() and self.current().isdigit():
            digit += self.consume()
        int_digit = int(digit)
        self.add_token(TokenType.NUMERIC, int_digit)




# class Parser: Takes a list of tokens and turns them into a list of expressions

# class Interpretor: Executes the expressions



