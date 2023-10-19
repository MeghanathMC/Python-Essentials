print(4+6)

print('Meghanath')  #print function always go to new line by default
print('Reddy')

print('Meghanath',end=' ')#end is  used to degine the next statement to be in the same line or next line
print('reddy')


a=3
b=4.23
print(a,b)

print(a,b,sep=" & ") #sep is used to seperate two variables
print(a,b,sep="\n")#\n helps in going into new line(however,by default it prints in new line)

#input functionality
# a=input()
# print("the number is ",a)

#to add two numbers(we had to typecast it to integer) as python takes input always in the form of string
num1 = int(input("enter 1st number\n"))
num2= int(input("enter 2nd number\n"))
print(num1,num2,sep="\n")
num3=num1+num2
print("result is ",num3)