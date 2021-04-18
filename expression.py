'''
The parser converts list of tokens into expressions
Every expression has an evaluate function
'''


class Expression:

    def evaluate(self):
        raise NotImplementedError("Please Implement this method")


class SelectPenExpression(Expression):

    def __init__(self, number=-1):
        self.pen_number = number

    def evaluate(self):
        if self.pen_number > -1:
            print(f"select pen {self.pen_number}")
        else:
            print("select pen")


class DrawWestExpression(Expression):

    def __init__(self, number=-1):
        self.cms = number

    def evaluate(self):
        if self.cms > -1:
            print(f"draw west {self.cms}cm")
        else:
            print("draw west")


class DrawNorthExpression(Expression):

    def __init__(self, number=-1):
        self.cms = number

    def evaluate(self):
        if self.cms > -1:
            print(f"draw north {self.cms}cm")
        else:
            print("draw north")


class DrawEastExpression(Expression):

    def __init__(self, number=-1):
        self.cms = number

    def evaluate(self):
        if self.cms > -1:
            print(f"draw east {self.cms}cm")
        else:
            print("draw east")

class DrawSouthExpression(Expression):

    def __init__(self, number=-1):
        self.cms = number

    def evaluate(self):
        if self.cms > -1:
            print(f"draw south {self.cms}cm")
        else:
            print("draw south")


class PenDownExpression(Expression):

    def evaluate(self):
        print("pen down")


class PenUpExpression(Expression):

    def evaluate(self):
        print("pen up")
