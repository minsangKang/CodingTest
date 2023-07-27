def solution(rank, attendance):
    nums = []
    for index, num in enumerate(rank):
        if attendance[index]:
            nums.append((num, index))
    nums = sorted(nums, key=lambda x: x[0])
    return 10000*nums[0][1] + 100*nums[1][1] + nums[2][1]