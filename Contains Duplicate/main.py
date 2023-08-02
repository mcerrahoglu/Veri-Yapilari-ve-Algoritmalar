nums = [1, 2, 3, 4, 5, 6]


def solution():
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] == nums[j]:
                    return True
    return False


print(solution())


def solution2():
    return len(nums) != len(set(nums))


print(solution2())


def solution3():
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


print(solution3())
