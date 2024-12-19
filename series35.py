import random

class Solution:
    def __init__(self, lst):
        self.lst = lst
        self.Lst = list()

    def make_lst(self):
        main_list = [i for i in range(0, 5)]
        idx_ = 0
        while idx_ < self.lst:
            tempo_lst = []
            idx = 0
            while True:
                random_element = random.choice(main_list)
                tempo_lst.append(random_element)
                if random_element == 0:
                    break
                idx += 1
            self.Lst.append(tempo_lst)
            idx_ += 1
        return self.Lst  ,[len(i) for i in self.Lst]


obj = Solution(4)

print(obj.make_lst())
