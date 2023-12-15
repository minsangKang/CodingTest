def solution(numbers):
    s = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            s.add(numbers[i]+numbers[j])    
    return sorted(list(s))