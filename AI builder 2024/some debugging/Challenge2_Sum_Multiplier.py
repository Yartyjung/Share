def summa(arr):
    sumX2= sum(arr)*2
    print(sumX2)
    for index in range(len(arr) - 1):
        for mul in range(index + 1, len(arr)):
            print(f"{mul} | {arr[index]} x {arr[mul]} = {arr[index] * arr[mul]}")
            if arr[index] * arr[mul] > sumX2:  
                print(f"There are answer more than {sumX2}")
                return "true"
    print(f"No answer more than {sumX2}")
    return "false"

# Test case 
print(summa([3, 2, 2, 2, 4, 1])) # False
print(summa([2, 5, 6, -6, 16, 2, 3, 6, 5, 3])) # True
    