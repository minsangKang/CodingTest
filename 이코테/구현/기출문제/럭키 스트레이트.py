# 럭키 스트레이트를 사용할 수 있는 상태인지 출력
nums = list(map(int, list(input())))
length = len(nums)
leftSum = sum(nums[:length//2])
rightSum = sum(nums[length//2:])
print("LUCKY" if leftSum == rightSum else "READY")