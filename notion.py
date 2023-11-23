# 노션작성내용 필터링 함수
def removeStar(str):
    str = str.replace("`**", "")
    str = str.replace("**`", "")
    return str

string = """"""
result = removeStar(string)
print(result)