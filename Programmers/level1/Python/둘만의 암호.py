def solution(s, skip, index):
    chars = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    return "".join([chars[(chars.index(i)+index)%len(chars)] for i in s])