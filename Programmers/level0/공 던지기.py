def solution(numbers, k):
    # 인덱스 계산법
    return numbers[2 * (k-1) % len(numbers)]
    # 숫자 계산법
    return 2 * (k-1) % len(numbers) + 1