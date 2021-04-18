from tokens import TokenType
from tokens import Token
from expression import *


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.expressions = []
        self.current_index = 0

    def parse(self):
        while not self.is_at_end():
            token = self.consume()
            if token.token_type == TokenType.KEYWORD:
                self.process_keyword(token)
            else:
                raise Exception(f"Unexpected token of type: {token.token_type} found expected type {str(TokenType.KEYWORD)}")
        return self.expressions

    def process_keyword(self, token):
        number = -1
        if self.current_token().token_type == TokenType.NUMERIC:
            number = self.consume().value
        if token.value == 'P':
            self.add_expression(SelectPenExpression(number))
        elif token.value == 'D':
            self.add_expression(PenDownExpression())
        elif token.value == 'W':
            self.add_expression(DrawWestExpression(number))
        elif token.value == 'N':
            self.add_expression(DrawNorthExpression(number))
        elif token.value == 'E':
            self.add_expression(DrawEastExpression(number))
        elif token.value == 'S':
            self.add_expression(DrawSouthExpression(number))
        elif token.value == 'U':
            self.add_expression(PenUpExpression())
        else:
            raise Exception(f"Token {token.value} not supported")

    def add_expression(self, expression):
        self.expressions.append(expression)

    def is_at_end(self):
        if self.current_token().token_type == TokenType.EOF:
            return True
        return False

    def current_token(self):
        return self.tokens[self.current_index]

    def advance(self):
        self.current_index = self.current_index + 1

    def consume(self):
        self.advance()
        return self.tokens[self.current_index - 1]






