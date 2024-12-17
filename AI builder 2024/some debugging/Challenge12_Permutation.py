import itertools as iT

def permutation(num) :
    number = num
    num = list(num)
    perm = iT.permutations(num)
    perm_joined = []
    
    for i in list(perm) :
        print(i)
        perm_joined.append(int("".join([str(j) for j in i])))
    
    perm_joined.sort()
    print(perm_joined)
    
    compare = int(number)
    last_max = max(perm_joined)+1
    current = None
    
    for i in perm_joined :
        if i > compare and i < last_max :
            current = i
            last_max = i
        else : pass
    if current is None : return "-1"
    else : return current
            
print(permutation("12131"))
print(permutation("12903"))