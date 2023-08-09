def solution(array):
    # 인덱스 -> 갯수인 배열, max값의 count를 통한 비교
    counts = [0]*1001
    for num in array:
        counts[num] += 1
    maxCount = max(counts)
    if counts.count(maxCount) > 1:
        return -1
    else:
        return counts.index(maxCount)
    # num -> 갯수인 dictionary, (갯수, num) 튜플배열의 정렬을 통한 비교
    dict = {}
    for num in array:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    result = sorted([(dict[key], key) for key in dict])
    if len(result) > 1 and result[-1][0] == result[-2][0]:
        return -1
    else:
        return result[-1][1]
        