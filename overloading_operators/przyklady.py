RANKS = ["szeregowy", "plutonowy", "sierżant", "podpułkownik", "pułkownik", "major"]

class Soldier:
    def __init__(self, rank):
        self.rank = rank

    def greater(self, other):
        return RANKS.index(self.rank) > RANKS.index(other.rank)
    def __gt__(self, other):
        return self.greater(other)

    pass

s1 = Soldier('szeregowy')
s2 = Soldier('major')


print(s1.greater(s2)) # False
print(s2.greater(s1)) # True
