
my_list = ["My name is ken", 420, 12.5]


my_list[0] = "My name is rakib"

for item in my_list:
    print(item)

del my_list[1]

print(len(my_list))

my_list.append(536)
print(my_list)

my_list.append(536)

print(my_list[0:2])

print(25*"-")

list1 = [1, "This is the list1", 3.5]
list2 = [True, "This is the list2", False]

list1.extend(list2)
print(list1)

list1.append('A new item')
list1.reverse()
print(list1)
