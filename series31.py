
list1 = [2, 3, 77, 9]
list2 = [4, 98, 99, 0]
list3 = [45, 54, 2, 90]

def find_two(lst):
    return True if 2 in lst else False

my_lists = [list1, list2, list3]
var = 0
for lst in my_lists:
    if find_two(lst):
        var += 1
print(var)


