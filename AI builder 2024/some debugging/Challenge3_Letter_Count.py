def LetterCountI(strParam):
    strParam = str(strParam).split(" ")
    for index,value in enumerate(strParam):
        print(f"Word | {value}")
        for char in list(value):
            if value.count(char) >= 2 :
                print(f"the duplicate letter is {char}")
                return strParam[index]
        print("no duplicate letter")
        print()
    return -1
        
print(LetterCountI('Today, is the greatest day ever!')) #greatest
print(LetterCountI('how did we get here')) # did
print(LetterCountI('how delight is that thing')) # that
