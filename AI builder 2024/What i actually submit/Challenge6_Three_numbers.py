def threeNum(string):
    lstring = string.split(' ')
    checker = []
    for index1, value in enumerate(lstring):
        temp = list(lstring[index1])
        comp = []
        for index2, value in enumerate(temp):
            if str(value).isnumeric():
                comp.append(value)
        print(temp,comp)
        if len(comp) >= 3:
            if comp[0] != comp[1] and comp[1] != comp[2]:       
                comparetor = ''.join([str(back) for back in comp])
                compared = ''.join([str(back) for back in lstring[index1]])
                if compared.find(comparetor) < 0 : checker.append(True)
                else : checker.append(False)
            else : checker.append(False)
        else : checker.append(False)
    for checker in checker :
        if checker == False : return "false"
    return "true" 
print(threeNum("2a3b5 w1o2rl3d g1gg92"))