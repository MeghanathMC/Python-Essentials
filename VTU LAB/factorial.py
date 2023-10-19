def fun(n):
    if n==1:
        return 0
    elif n==2:
        return 1

    else:
        return fun(n-1)+fun(n-2)

num=int(input("enter a number: "))
if num>0:
    res = fun(num)
    print("fibonnoci of given number ","fun(",num,")=",res)
else:
    print("error in input")