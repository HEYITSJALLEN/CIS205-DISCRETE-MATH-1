my_set = {1, 2, 3}
my_set.pop()
print(len(my_set))

my_set = {1, 2, 3}
my_set.discard(4)
print(my_set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
symmetric_diff = set_a.symmetric_difference(set_b)
print(symmetric_diff)