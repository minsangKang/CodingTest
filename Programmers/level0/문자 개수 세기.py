def solution(my_string):
    array = [0]*52
    for s in my_string:
        if s.isupper():
            array[ord(s)-ord('A')] += 1
        else:
            array[ord(s)-ord('a')+26] += 1
    return array