def solution(todo_list, finished):
    return [todo for i, todo in enumerate(todo_list) if finished[i] == False]