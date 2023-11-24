def solution(s, skip, index):
    chars = list(filter(lambda x: x not in skip, [chr(i) for i in range(ord('a'), ord('z')+1)]))
    return "".join([chars[(chars.index(char)+index)%len(chars)] for char in s])