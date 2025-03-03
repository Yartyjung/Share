def NoPair(Input):
    map = []
    Input = "".join(str(i) for i in Input)
    for i in Input:
        map.append(Input.count(i))
    # print(map.index(1))
    return Input[map.index(1)]


print(NoPair([7, 1, 2, 7, 1]))
print(NoPair([1, 1, 3, 3, 4, 4, 4, 9, 1, 4, 1]))
