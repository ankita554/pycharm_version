some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

my_list = sorted(some_list)

duplicates = []
for i in my_list:
    if my_list.count(i) > 1:

     if i not in duplicates:

         duplicates.append(i)

print(len(duplicates))
print(duplicates)
print("name_ankita")


def test_add(a,b):

    return a+b

print(test_add(4,5))
print(test_add(56,23))