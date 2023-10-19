val=input("enter a value:")
if val==val[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")

for i in range(10):
    if val.count(str(i))>0:
        print(str(i),"appears",val.count(str(i)),"times")
