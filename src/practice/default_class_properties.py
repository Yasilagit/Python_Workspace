class Example:
    'Common base class for all employee'
    def printValue(self):
        print(Example.__doc__)
        print(Example.__name__)
        print(Example.__dict__)
        print(Example.__module__)
        print(Example.__bases__)
example = Example()
example.printValue()

