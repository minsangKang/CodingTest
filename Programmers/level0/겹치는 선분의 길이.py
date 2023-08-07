def solution(lines):
    # point 1: 선분의 끝점끼리 겹쳐봤자 선분이 겹쳐지지 않으므로 이를 판별하기 위해 선분의 시작점은 포함, 끝점은 미포함하는 구간으로 계산한다.
    # point 2: 그러면 겹치는것끼리의 합집합을 구하면 끝
    A, B, C = [set(range(start, end)) for start, end in lines]
    return len(A&B|A&C|B&C)

    # 악으로 깡으로 푼 코드
    A = set(range(lines[0][0], lines[0][1]+1))
    B = set(range(lines[1][0], lines[1][1]+1))
    C = set(range(lines[2][0], lines[2][1]+1))
    A_B, A_C, B_C = A&B, A&C, B&C
    print(A_B, A_C, B_C)
    result = 0
    if len(A_B) > 1:
        result += len(A_B)-1
    if len(A_C) > 1:
        result += len(A_C)-1
    if len(B_C) > 1:
        result += len(B_C)-1
    
    AmB, AmC, BmC = A_B&A_C, A_B&B_C, A_C&B_C
    if len(AmB) > 1:
        result -= len(AmB)-1
    if len(AmC) > 1:
        result -= len(AmC)-1
    if len(BmC) > 1:
        result -= len(BmC)-1
    
    AandBandC = AmB&AmC&BmC
    if len(AandBandC) > 1:
        result += len(AandBandC)-1
        
    return result