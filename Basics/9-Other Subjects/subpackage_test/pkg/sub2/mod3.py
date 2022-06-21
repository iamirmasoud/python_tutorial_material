def foo3():
    print("foo3")


class Foo3:
    def __init__(self):
        print("Foo 3 class")


from pkg.sub1.mod1 import foo1

foo1()
