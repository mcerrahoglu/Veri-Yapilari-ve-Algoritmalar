nums = [1, 2, 1, 2, 3]


def solution():
    result = 0
    for i in nums:
        result = i ^ result
    return result


print(solution())

# bit manipulation methods
# xor gate
