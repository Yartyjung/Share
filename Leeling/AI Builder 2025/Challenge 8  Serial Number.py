test1: str = "11.124.667"
test2: str = "114.568.112"


def SerialNumber(Str):
    # sum function
    def Sum(Str, max_position=3):
        temp = 0
        for i in range(max_position):
            temp += int(Str[i])
        return temp

    # main code
    Str = Str.split(".")
    for i in Str:
        if len(i) < 3:
            return False
    if Sum(Str[0]) % 2 > 0:
        return False
    if Sum(Str[0]) % 2 < 0:
        return False
    if int(Str[0][0]) > int(Str[0][2]) and int(Str[0][1]) > int(Str[0][2]):
        return False
    if int(Str[1][0]) > int(Str[1][2]) and int(Str[1][1]) > int(Str[1][2]):
        return False
    else:
        return True


print(SerialNumber(test2))
