#32-masala
import random

from oy2darslar.oy2dars4 import make_lst


class Solution:
    def __init__(self, num, lst):
        self.num = num
        self.lst = lst
        self.Lst = list()

    def make_lst(self):
        main_list = [i for i in range(1, 10)]
        idx_ = 0
        while idx_ < self.lst:
            tempo_lst = []
            idx = 0
            while idx < self.num:
                random_element = random.choice(main_list)
                tempo_lst.append(random_element)
                idx += 1
            self.Lst.append(tempo_lst)
            idx_ += 1
        return self.Lst

    def get_index(self):
        indeces = []
        for i in self.Lst:
            if 2 in i:
                indeces.append(i.index(2))
            else: indeces.append(0)
        return indeces



obj = Solution(4, 3)

print(obj.make_lst())
print(obj.get_index())


