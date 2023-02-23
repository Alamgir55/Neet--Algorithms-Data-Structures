
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


def is_palidom(s):
    orgain_string = s
    fun_revers = reverse(s)
    if orgain_string == fun_revers:
        return True

    return False


def reverse(data):
    data = list(data)
    startIndex = 0
    endIndex = len(data) - 1

    while endIndex > startIndex:
        data[startIndex], data[endIndex] = data[endIndex], data[startIndex]
        startIndex = startIndex + 1
        endIndex = endIndex - 1

    return ''.join(data)


if __name__ == '__main__':
    print(is_palidom('car'))
