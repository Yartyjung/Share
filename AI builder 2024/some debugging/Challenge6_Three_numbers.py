def threeNum(string):
    lstring = string.split(' ')
    checker = []
    for index, value in enumerate(lstring):
        temp = list(lstring[index])
        comp = []
        for value in temp:
            if str(value).isnumeric():
                comp.append(value)
        print(temp)
        print(comp)
        print()
        
        if len(comp) >= 3: # if there are less than 3 charecter then it's an edge case
            if comp[0] != comp[1] and comp[1] != comp[2]:        
                comparetor = ''.join([str(back) for back in comp])
                compared = ''.join([str(back) for back in lstring[index]])
                print(comparetor, compared)
                if compared.find(comparetor) < 0 : pass # just to be sure ,the .find will return -1 if it can't find it instance 
                else : return False
            else : return False
        else : return False
    return "true" 
print(threeNum("2a3b5 w1o2rl3d g1gg92"))