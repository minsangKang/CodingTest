# A, E, I, O, U
words = ["A", "E", "I", "O", "U"]
jump5 = 1
jump4 = 5*jump5+1
jump3 = 5*jump4+1
jump2 = 5*jump3+1
jump1 = 5*jump2+1
jumps = [jump1, jump2, jump3, jump4, jump5]

def solution(word):
    answer = 0
    for i in range(len(word)):
        answer += 1 # A의 경우 +1 상태
        answer += words.index(word[i]) * jumps[i]
    return answer

answer = solution("I")
print(answer)