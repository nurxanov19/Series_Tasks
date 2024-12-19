import random

class Solution:
    def __init__(self, lst):
        self.lst = lst
        self.Lst = list()

    def make_lst(self):
        idx_ = 0
        while idx_ < self.lst:
            tempo_lst = []
            min_val, max_val = 1, 5

            while True:
                random_element = random.choice(range(min_val, max_val))
                tempo_lst.append(random_element)
                if random_element == 0:
                    break
                min_val = 0

            self.Lst.append(tempo_lst)
            idx_ += 1
        return self.Lst, [1 if sorted(i[:-1]) == i[:-1] else -1 if sorted(i, reverse=True) == i else 0 for i in self.Lst]



obj = Solution(4)

print(obj.make_lst())