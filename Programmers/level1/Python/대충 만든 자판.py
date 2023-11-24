def solution(keymap, targets):
    dict = {}
    for chars in keymap:
        for idx, char in enumerate(chars):
            if char in dict:
                dict[char] = min(dict[char], idx+1)
            else:
                dict[char] = idx+1
    
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
            