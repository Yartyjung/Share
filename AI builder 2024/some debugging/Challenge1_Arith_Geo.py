def ArithGeo(arr):
    
    check_arithmetic = []
    check_geometric = [] 
    arr_size = len(arr)-1
    
    for index, value in enumerate(arr):
        if arr_size > index :
            check_arithmetic.append(arr[index] - arr[index + 1])
            check_geometric.append(arr[index+1] / arr[index])
    
    print(f"check arithmetic | {check_arithmetic}")
    print(f"check geometric  | {check_geometric}")
    print()
    
    for index , _ in enumerate(check_arithmetic) :
        if check_arithmetic[index] != check_arithmetic[index + 1] and arr_size > index :
            for index, value in enumerate(check_geometric) :
                if check_geometric[index] != check_geometric[index+1] and arr_size > index :
                    return "-1"
                else :
                    return "Geometric"
        else : 
            return "Arithmetic"
        
# Test case 
print(ArithGeo([2,4,16,24])) # -1
print(ArithGeo([1,6,90,28])) # -1
print(ArithGeo([1,2,4,8])) # Geometric
print(ArithGeo([3,6,12,24])) # Geometric
print(ArithGeo([1,1,1,1])) # Arithmetic
print(ArithGeo([9,12,15,18])) # Arithmetic