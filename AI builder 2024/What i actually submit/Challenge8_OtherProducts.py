import numpy
def otherProducts(arr) :
    result = []
    for i in range(0,len(arr)):
        poped = arr.pop(i)
        result.append(numpy.prod(arr))
        print(arr,poped)
        arr.insert(i,poped)
        str_result = "-".join([str(i) for i in result])
    return str_result
        
        

print(otherProducts([1,2,3,4,5,6,7,8,9,10]))