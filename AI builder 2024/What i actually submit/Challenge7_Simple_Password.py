def SimplePassword(passw):
    lstring = list(passw)
    check_list = [",",".",":",";","\"","'","_","-","(",")","[","]","/","?","!","=","+","*","#","@","$","%","&","<",">","{","}","^","~","`"]
    checker = [False,False,False] #uppercase,numeric,punctuation
    if str(passw).casefold().find("password") > -1 : return "false"
    if len(str(passw)) > 7 and len(str(passw)) < 31 :
        for index,value in enumerate(lstring):
            if value.isupper() : checker[0] = True
            elif value.isnumeric() : checker[1] = True
            elif value in check_list : checker[2] = True          
    else : return "false"
    re = checker[0]=checker[1]=checker[2]
    if re == True : return "true"

# keep this function call here 
print(SimplePassword("passord2daasdWWWW()/+"))#asdasdasdaasdasdasdaasdasdasdaasdasdasda passord2daasdWWWW()/+