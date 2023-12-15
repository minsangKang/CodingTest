def solution(numbers, hand):
    dict = {
        '1':(1,1), '2':(1,2), '3':(1,3),
        '4':(2,1), '5':(2,2), '6':(2,3),
        '7':(3,1), '8':(3,2), '9':(3,3),
        '*':(4,1), '0':(4,2), '#':(4,3)
    }
    lefts = ['1', '4', '7']
    rights = ['3', '6', '9']
    lpos, rpos = dict['*'], dict['#']
    
    result = ""
    
    for n in numbers:
        if str(n) in lefts:
            result += 'L'
            lpos = dict[str(n)]
        elif str(n) in rights:
            result += 'R'
            rpos = dict[str(n)]
        else:
            ldist = dist(lpos, dict[str(n)])
            rdist = dist(rpos, dict[str(n)])
            if ldist < rdist:
                result += 'L'
                lpos = dict[str(n)]
            elif ldist > rdist:
                result += 'R'
                rpos = dict[str(n)]
            else:
                if hand == 'left':
                    result += 'L'
                    lpos = dict[str(n)]
                else:
                    result += 'R'
                    rpos = dict[str(n)]
        
        return result
            
def dist(from, to):
    return abs(from[0]-to[0]) + abs(from[1]-to[1])