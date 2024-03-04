#!/usr/bin/env python3

class Shoe:
    '''Shoe class'''

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

from shoe import Shoe


stan_smith = Shoe("lv red ", 9)

print("Brand:", stan_smith.brand)
print("Size:", stan_smith.size)
print("Condition:", stan_smith.condition)

stan_smith.cobble()


print("Condition after cobbling:", stan_smith.condition)
