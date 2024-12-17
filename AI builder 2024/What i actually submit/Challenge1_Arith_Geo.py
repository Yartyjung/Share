def ArithGeo(arr):
    checker_arith = []
    checker_geo = [] 
    for index, value in enumerate(arr):
        if len(arr)-1 > index :
            checker_arith.append(arr[index] - arr[index + 1])
            checker_geo.append(arr[index+1] / arr[index])
    for index, value in enumerate(checker_arith) :
        if checker_arith[index] != checker_arith[index + 1] and len(arr)-1 > index :
            for index, value in enumerate(checker_geo) :
                if checker_geo[index] != checker_geo[index+1] and len(arr)-1 > index : return "-1"
                else : return "Geometric"
        else : return "Arithmetic"
# keep this function call here 
print(ArithGeo([2,4,16,24]))