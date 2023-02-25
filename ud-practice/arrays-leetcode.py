
# def reverse(nums):
#     startIndex = 0
#     endIndex = len(nums) - 1

#     while endIndex > startIndex:
#         nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
#         startIndex = startIndex + 1
#         endIndex = endIndex - 1


# if __name__ == '__main__':
#     n = [1, 2, 3, 4, 5]
#     reverse(n)
#     print(n)


# def is_palidom(s):
#     orgain_string = s
#     fun_revers = reverse(s)
#     if orgain_string == fun_revers:
#         return True

#     return False


# def reverse(data):
#     data = list(data)
#     startIndex = 0
#     endIndex = len(data) - 1

#     while endIndex > startIndex:
#         data[startIndex], data[endIndex] = data[endIndex], data[startIndex]
#         startIndex = startIndex + 1
#         endIndex = endIndex - 1

#     return ''.join(data)


# if __name__ == '__main__':
#     print(is_palidom('car'))

# def reverse_integer(n):
#     reverse_integer = 0
#     reminder = 0

#     while n > 0:
#         reminder = n % 10
#         reverse_integer = reverse_integer * 10 + reminder
#         n = n // 10

#     return reverse_integer


# print(reverse_integer(1234))

# def anagram_fun(str1, str2):

#     if len(str1) != len(str1):
#         return False

#     str1 = sorted(str1)
#     str2 = sorted(str2)

#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             return False

#     return True


# s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
# s2 = ['r', 'e', 's', 't', 'f', 'u', 'l']
# print(anagram_fun(s1, s2))


# def duch_flag_problem(nums, pivot=1):
#     i = 0
#     j = 0
#     k = len(nums) - 1

#     while j <= k:
#         if nums[j] < pivot:
#             swap(nums, i, j)
#             i = i + 1
#             j = j + 1
#         elif nums[j] > pivot:
#             swap(nums, j, k)
#             k = k - 1
#         else:
#             j = j + 1

#     return nums


# def swap(nums, index1, index2):
#     nums[index1], nums[index2] = nums[index2], nums[index1]


# print(duch_flag_problem([0, 1, 2, 2, 1, 0, 0, 2, 2, 1]))

# # print(duch_flag_problem([4, 4, 5, 5, 3, 3, 3]))

def trapping_water_problem(heights):
    if len(heights) < 3:
        return 0

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # dealing with the left max values
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    # dealing with the right max values
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i + 1])

    # consider all the items in O(N) and sum up the trapped rain water units
    trapped = 0

    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i]) - heights[i]

    return trapped


if __name__ == '__main__':
    print(trapping_water_problem([1, 0, 2, 1, 3, 1, 2, 0, 3]))
