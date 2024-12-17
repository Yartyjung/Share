def SimplePassword(passw):
    lstring = list(passw)
    check_list = [",",".",":",";","\"","'",'"',"_","-","(",")","[","]","/","?","!","=","+","*","#","@","$","%","&","<",">","{","}","^","~","`"]
    requirement = [False,False,False] #uppercase,numeric,punctuation
    
    if str(passw).casefold().find("password") > -1 : return "false" # check is there a word "password" in the password
    
    if len(str(passw)) > 7 and len(str(passw)) < 31 : # Check the lenght of the passwoed
        for index,value in enumerate(lstring):
            if value.isupper() : requirement[0] = True #Check for Capitalize charecter
            elif value.isnumeric() : requirement[1] = True #Check for number
            elif value in check_list : requirement[2] = True #Check is there any check_list charecter
    
    else : return "false"
    
    requirement_met = requirement[0]=requirement[1]=requirement[2]
    
    if requirement_met == True : return "true"

# keep this function call here 
print(SimplePassword("passord2daasdWWWW()/+"))