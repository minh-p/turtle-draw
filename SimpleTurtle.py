import turtle

class SimpleTurtle:
    def __init__(self, shape="turtle"):
        self.stateChange = turtle.Turtle()
        self.stateChange.shape = shape
        self.stateChange.pensize(3)

    def exitonclick(self):
        turtle.exitonclick()

    def alter(self, operations):
        # operations = [[direction, distance]]
        for operation in operations:
            directionString = operation[0]

            movementMethod = None
            try:
                movementMethod = getattr(self.stateChange, directionString)
            except:
                raise NameError("Alter method not applicable. You may want a correct direction or method.")

            if len(operation) == 2:
                movementMethod(operation[1])
            else:
                movementMethod()
