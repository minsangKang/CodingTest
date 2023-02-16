# 알파벳 오름차순 정렬 + 숫자합 출력
inputs = input()
chars = []
sum = 0
for i in inputs:
    if i.isalpha():
        chars.append(i)
    else:
        sum += int(i)
chars.sort()
print("".join(chars) + str(sum))