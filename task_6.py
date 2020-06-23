from itertools import count
from itertools import cycle

n = int(input("Введите число "))

for el in count(n):
    if el > 15:
        break
    else:
        print(el)


my_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1
