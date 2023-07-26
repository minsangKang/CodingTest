def solution(a, b, c, d):
    dict = {}
    for num in [a, b, c, d]:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
            
    nums = set([a, b, c, d])
    if len(nums) == 1:
        return 1111*a
    elif len(nums) == 4:
        return min([a, b, c, d])
    elif len(nums) == 2:
        # 3, 1 쌍
        numbers = list(nums)
        if dict[numbers[0]] == 1 and dict[numbers[1]] == 3:
            return (10*numbers[1]+numbers[0])**2
        elif dict[numbers[0]] == 3 and dict[numbers[1]] == 1:
            return (10*numbers[0]+numbers[1])**2    
        # 2, 2 쌍
        elif dict[numbers[0]] == 2 and dict[numbers[1]] == 2:
            return (numbers[0]+numbers[1])*abs(numbers[0]-numbers[1])
    # 2, 1, 1 쌍
    elif len(nums) == 3:
        numbers = list(nums)
        for num in numbers:
            if dict[num] == 2:
                numbers.strip(num)
                return numbers[0]*numbers[1]
        
print(solution(6, 4, 2, 5))