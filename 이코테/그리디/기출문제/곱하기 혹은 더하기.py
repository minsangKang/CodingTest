# 만들어질 수 있는 가장 큰 수
nums = input()
result = int(nums[0])
for i in range(1, len(nums)):
    num = int(nums[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)