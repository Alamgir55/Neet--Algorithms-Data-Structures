numbers = [1, -5, 0, 10, 100, 67, 55, 20, 34]

names = ['Adam', 'Kevin', 'Anna', 'Joe', 'Danial', 'Bill']
# new_list = [num for num in numbers if num % 2 == 0]

# for nums in numbers:
#     if nums % 2 == 0:
#         new_list.append(nums)

filter_name = [name for name in names if len(name) == 4]

# for name in names:
#     if name.startswith('A'):
#         filter_name.append(name)

print(filter_name)
