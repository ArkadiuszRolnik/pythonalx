

Napisz funkcję, która pozwoli na dodawanie do siebie macierzy.

Funkcja przyjmuje jako argumenty macierze i zwraca ich sumę

1. Zacznij od dodania dwóch argumentów

    >>> matrix1 = [[1, -2], [-3, 4]]

    >>> matrix2 = [[2, -1], [0, -1]]

    >>> add(matrix1, matrix2)

    [[3, -3], [-3, 3]]

    >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

    >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

    >>> add(matrix1, matrix2)

    [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]



2. Pozwól jej przyjmować więcej macierzy jako argumenty

    >>> add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]])

    [[8, 8], [7, 7]]



3. Jeśli wymiary macierzy nie są zgodne powinien zostać rzucony wyjątek ValueError:

    >>> add([[1, 9], [7, 3]], [[1, 2], [3]])

    Traceback (most recent call last):

    File "<stdin>", line 1, in <module>

    File "add.py", line 10, in add

    raise ValueError("Given matrices are not the same size.")

    ValueError: Given matrices are not the same size.

