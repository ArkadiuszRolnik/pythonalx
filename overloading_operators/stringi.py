class MyInt:

    def __init__(self, repr: str):
        self.repr = repr
        self.i = int(self.repr)

    def __add__(self, other):
        if isinstance(other, int):
            return MyInt(str(other + self.i))
        return MyInt(str(self.i + other.i))

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        return self.i == other.i

    def __sub__(self, other):
        return MyInt(str(self.i - other.i))

    def __str__(self):
        return f"<MyInt: {self.repr}>"

n0 = MyInt("10")
n1 = MyInt("10")

print(n0 == n1)
assert n0 == n1

n1 = MyInt("10")
n2 = MyInt("12")

assert n1 + n2 == MyInt("22")
assert n1 - n2 == MyInt("-2")

