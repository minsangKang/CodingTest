def solution(my_string):
    chars = list(my_string)
    for index, char in enumerate(chars):
        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            continue
        else:
            chars[index] = ' '
    newChars = "".join(chars).split()
    return sum(int(num) for num in newChars)