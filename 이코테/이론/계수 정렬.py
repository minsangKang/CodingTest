def sort(array):
    counts = [0]*(max(array)+1)
    
    for i in range(len(array)):
        counts[array[i]] += 1

    sorted = []
    for i in range(len(counts)):
        sorted += [i] * counts[i]

    return sorted

print(sort([3, 5, 1, 2, 9, 6, 4, 7, 5]))

data = [("바나나", 2), ("당근", 3)]
data.sort(key=lambda x : (x[0], x[1]))
print(data)