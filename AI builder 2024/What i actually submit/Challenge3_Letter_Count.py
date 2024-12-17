def LetterCountI(strParam):
    strParam = str(strParam).split(" ")
    for index,value in enumerate(strParam):
        for char in list(value):
            if value.count(char) >= 2 :
                return strParam[index]
    return -1
        
print(LetterCountI(input()))