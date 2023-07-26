def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    maxCount = max(counts)

    if maxCount == 4:
        return 1111*a
    elif maxCount == 1:
        return min(nums)
    elif maxCount == 3:
        return (10*nums[counts.index(3)]+nums[counts.index(1)])**2
    elif maxCount == 2:
        # 2, 2쌍
        if min(counts) == 2:
            numbers = list(set(nums))
            return (numbers[0]+numbers[1])*abs(numbers[0]-numbers[1])
        # 2, 1, 1쌍
        else:
            numbers = []
            for i in range(4):
                if counts[i] == 1:
                    numbers.append(nums[i])
            return numbers[0]*numbers[1]