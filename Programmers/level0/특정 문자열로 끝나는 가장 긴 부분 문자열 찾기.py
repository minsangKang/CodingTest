def solution(myString, pat):
    firstIndexOfReverse = myString[::-1].index(pat[::-1])
    return myString[:len(myString) - firstIndexOfReverse]