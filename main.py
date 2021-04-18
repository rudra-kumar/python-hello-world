from scanner import Scanner
from parser import Parser
from expression import Expression


def main():
    scanner = Scanner("P 2 D W 2 N 1 E 2 S 1 U")
    tokens = scanner.scan()
    parser = Parser(tokens)
    expressions = parser.parse()
    for expression in expressions:
        expression.evaluate()


if __name__ == "__main__":
    main()
