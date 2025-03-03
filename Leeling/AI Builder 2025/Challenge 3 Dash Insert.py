def DashInsert(Str):
    list = []
    output = []
    list = list.append(i for i in Str)
    for i, v in enumerate(Str):
        if i == 0:
            output.append(v)
        if i > 0:
            if int(Str[i - 1]) % 2 != 0 and int(Str[i]) % 2 != 0 and int(v) != 0:
                output.append(v)
                output.insert(len(output) - 1, "-")
            if int(Str[i - 1]) % 2 == 0 and int(Str[i]) % 2 != 0 and int(v) != 0:
                output.append(v)
            if int(v) % 2 == 0:
                output.append(v)
    return "".join(str(x) for x in output)


print(DashInsert(str(56730)))
print(DashInsert(str(99946)))
print(DashInsert(str(454793)))
