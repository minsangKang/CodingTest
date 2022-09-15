def sort(array, reverse):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    if reverse == True:
        return left_side + [pivot] + right_side
    else:
        return right_side + [pivot] + left_side

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
numbers = sort(numbers, True)
for n in numbers:
    print(n, end=" ")
print()