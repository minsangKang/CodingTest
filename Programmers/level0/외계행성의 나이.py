def solution(age):
    dict = { str(i): chr(i+ord('a')) for i in range(10) }
    return "".join([dict[i] for i in str(age)])