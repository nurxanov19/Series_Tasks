import random

class Solution:
    def __init__(self, num, lst):
        self.num = num
        self.lst = lst
        self.Lst = list()

    def make_lst(self):
        main_list = [i for i in range(1, 5)]
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
                indeces.append(sum(i))
        return indeces



obj = Solution(4, 3)

print(obj.make_lst())
print(obj.get_index())