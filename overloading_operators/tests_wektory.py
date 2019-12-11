from wektory import Vector

class TestVector:

    def test_create_vector(self):
        v1 = Vector(x = 1, y = 2)
        assert True

    def test_add_(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 2)
        v = v1 + v2
        assert v.x == 3

