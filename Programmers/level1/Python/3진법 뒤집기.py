def solution(n):
    zin3 = trans(n, 3)
    reverse3 = zin3[::-1]
    return int(reverse3, 3)

# 진수변환기
def trans(a, b):
    arr = []
    n = a
    while n != 0:
        arr.append(str(n%b))
        n //= b
    return "".join(arr[::-1])