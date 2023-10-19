# a='meghanath'
# print(type(a))
# b="""meghanath     #using mutliple quotes while assigning a string value to varible is valid
# is learning"""
# print(b,sep='')
# #indexing is very important in python
# #indexing always start from 0
# #we can also use negative indexing from reverse side
# print(b[1])
# print(b[-1])
# # b[0]='r' #cannot be modified
# # print(b)
# print(len(a))

a='the oxford college of engineering'
print(a[5])
print(a.capitalize()) #keeps first letter caps
print(a.upper()) #coverts all the letters to upper case
print(a.lower()) #convert all the letters to lower case
print(a.count('e')) #counts the no. of time the letter is repeated
print(a.replace('engineering','management')) #this will replace a particular word with another word
print(len(a)) #this will find the length of string
print(a.find('the')) #this will return the index of first letter in a word
print(a.casefold())
print(a.endswith('ring')) #this checks whether the string ends with particular letters
print(a.__contains__('college')) #this checks whether the string contain that word or not
print(a.startswith('t')) #checks wheter it starts with partcular letter
print(a*2)#this prints the string 2 times
print(a+2) #we cannot concatenate the string with int(this throw an error)
