import re


def isphonenumber(num):
    if len(num)!=12:
        return False
    for i in range(12):
        if i==3 or i==7:
            if num[i]!='-':
                return False
            else:
                if num[i].isdigit==False:
                    return False
    return True

def checkphonenumber(num):
    ph_no_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}-$')
    if ph_no_pattern.match(num):
        return True
    else:
        return False



ph_num=input("enter a phone number")
print("without using regular expression")
if isphonenumber(ph_num):
    print("valid phone number")
else:
    print("invalid phone number")

print("with using regular expression")
if checkphonenumber(ph_num):
    print("valid phone number")
else:
    print("invalid phone number")