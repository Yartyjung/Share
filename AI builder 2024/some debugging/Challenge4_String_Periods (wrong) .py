"this one is fuckup don't read it "
def StringPeriods(s):
    if len(s) == 1:
        return -1
    def repeat(sub_str, s):
        repeated_str = sub_str * ((len(s) // len(sub_str)) + 1)
        return repeated_str.startswith(s)
    longest_substr = ''
    half_length = len(s) // 2
    for i in range(1, half_length + 1):
        sub_str = s[:i]
        if repeat(sub_str, s) : longest_substr = sub_str
    if longest_substr == '':
        return -1
    return longest_substr



print(StringPeriods("abababababababa"))  
print(StringPeriods("abababababab"))      
# print(StringPeriods("aaaaa"))             
