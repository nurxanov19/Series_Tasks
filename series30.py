
n, k = 5, 3  # 5 ta sondan iborat 3 ta to'plam

def elem_sum(n, k):
    idx, elem = 0, 1
    while idx < k:
        my_list = []
        for _ in range(n):
            my_list.append(elem)
            elem += 1
        idx += 1
        print(f"{idx} inchi list elementlari yig'indisi: {sum(my_list)}")

elem_sum(n, k)