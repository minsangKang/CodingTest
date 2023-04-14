from bisect import bisect_left, bisect_right

# 배열 내 leftValue 이상 rightValue 이하 개수 반환
def count_by_range(array, leftValue, rightValue):
    leftIndex = bisect_left(array, leftValue)
    rightNextIndex = bisect_right(array, rightValue)
    return rightNextIndex - leftIndex

# 키워드 길이별 배열 생성 (정방향, 역방향)
arrayOfSizes = [[] for _ in range(10001)]
reversedArrayOfSizes = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    
    # 각 word 를 길이별 정방향, 역방향 배열 내 추가
    for word in words:
        size = len(word)
        arrayOfSizes[size].append(word)
        reversedArrayOfSizes[size].append(word[::-1])
        
    # 이진탐색을 위해서 sort
    for i in range(10001):
        arrayOfSizes[i].sort()
        reversedArrayOfSizes[i].sort()
        
    # 모든 쿼리 확인
    for query in queries:
        size = len(query)
        
        # ?로 끝나는 query -> ? 를 a, z로 변환
        if query[0] != '?':
            leftValue = query.replace('?', 'a')
            rightValue = query.replace('?', 'z')
            count = count_by_range(arrayOfSizes[size], leftValue, rightValue)
            answer.append(count)
        # ?로 시작하는 query -> reverse 후 ? 를 a, z로 변환
        else:
            leftValue = query[::-1].replace('?', 'a')
            rightValue = query[::-1].replace('?', 'z')
            count = count_by_range(reversedArrayOfSizes[size], leftValue, rightValue)
            answer.append(count)

    return answer