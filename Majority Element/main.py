nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3]


def solution():
    numbers = {}
    result = 0
    maxnumber = 0
    for num in nums:
        numbers[num] = 1 + numbers.get(num, 0)
        if numbers[num] > maxnumber:
            result = num
        maxnumber = max(maxnumber, numbers[num])
    return result


def solution2():
    result = nums[0]
    counter = 0
    for num in nums:
        if result == num:
            counter = counter + 1
        elif result != num:
            counter = counter - 1
        if counter == 0:
            result = num
            counter = counter + 1
    return result


print(solution())
print(solution2())
