# A: min, B: max 서로 교환
def swapForMaxArrayA(arrA, arrB, K):
    for i in range(K):
        if arrA[i] < arrB[i]:
            arrA[i], arrB[i] = arrB[i], arrA[i]
        else:
            break

N, K = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
arrA.sort()
arrB.sort(reverse=True)
swapForMaxArrayA(arrA, arrB, K)

print(sum(arrA))
