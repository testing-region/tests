# import list from Part 2
from Part2 import my_list


my_list = my_list + ["apple", 76]

# index = position - 1
# 3rd position = index 2
my_list.insert(2, 'cat')
my_list.insert(0, 99)

index_of_hello = my_list.index("hello")
count_76 = my_list.count(76)

my_list.remove(76)

my_list.pop(my_list.index(True)) 