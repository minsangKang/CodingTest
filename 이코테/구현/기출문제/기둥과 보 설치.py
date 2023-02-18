# 최종 구조물의 상태를 x좌표 오름차순 -> y좌표 오름차순 -> 기둥 -> 보 순으로 정렬 [x, y, a]
# a: 0=기둥, 1=보
# b: 0=삭제, 1=설치

# 현재 설치된 구조물이 가능한 구조물인지 확인
def possible(answers):
    STICK = 0
    TABLE = 1
    for x, y, obj in answers:
        # 기둥인 경우
        if obj == STICK:
            # 바닥 위인 경우
            if y == 0:
                continue
            # 보의 좌측 끝 위인 경우
            elif [x-1, y, 1] in answers:
                continue
            # 보의 우측 끝 위인 경우
            elif [x, y, 1] in answers:
                continue
            # 기둥 위인 경우
            elif [x, y-1, 0] in answers:
                continue
            else:
                return False
        # 보인 경우
        elif obj == TABLE:
            # 좌측 끝이 기둥 위인 경우
            if [x, y-1, 0] in answers:
                continue
            # 우측 끝이 기둥 위인 경우
            elif [x+1, y-1, 0] in answers:
                continue
            # 양끝이 보인 경우
            elif ([x-1, y, 1] in answers and [x+1, y, 1] in answers):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    DELETE = 0
    CREATE = 1
    # 구조물 전체
    answers = []
    for frame in build_frame:
        x, y, obj, operate = frame
        if operate == DELETE:
            answers.remove([x, y, obj])
            if not possible(answers):
                answers.append([x, y, obj])
        elif operate == CREATE:
            answers.append([x, y, obj])
            if not possible(answers):
                answers.remove([x, y, obj])

    answers.sort()
    return answers
    

# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]