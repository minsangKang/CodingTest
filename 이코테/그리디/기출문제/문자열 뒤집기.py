# 모든 숫자가 같도록 뒤집는 최소횟수
nums = input()
zeroCount = 0
oneCount = 0
if nums[0] == '0':
    zeroCount += 1
else:
    oneCount += 1

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        # 횟수 증가
        if nums[i+1] == '0':
            zeroCount += 1
        else:
            oneCount += 1

print(min(zeroCount, oneCount))
