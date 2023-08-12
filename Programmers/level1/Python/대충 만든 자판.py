def solution(keymap, targets):
    dict = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dict:
                dict[k] = i+1
            else:
                dict[k] = min(dict[k], i+1)
                
    result = []
    for target in targets:
        count = 0
        for t in target:
            if t not in dict:
                count = -1
                break
            count += dict[t]
        result.append(count)
    
    return result