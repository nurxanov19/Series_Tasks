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
        return self.Lst, [i[:-1] for i in self.Lst if sorted(i[:-1]) == i[:-1] or sorted(i, reverse=True) == i ]



obj = Solution(4)

print(obj.make_lst())