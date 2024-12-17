def summa(arr):
    sumx2= sum(arr)*2
    for index in range(len(arr) - 1):
        for mul in range(index + 1, len(arr)):
            if arr[index] * arr[mul] > sumx2:
                return "true"
    return "false"
print(summa([3, 2, 2, 2, 4, 1]))
    