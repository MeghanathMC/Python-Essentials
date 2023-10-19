m1=int(input("enter marks of sub1: "))
m2=int(input("enter marks of sub2: "))
m3=int(input("enter marks of sub3: "))
if m1<=m2 and m1<=m3:
    avg=(m2+m3)/2
elif m2<=m3 and m2<=m1:
    avg=(m1+m3)/2
elif m3<=m1 and m3<=m2:
    avg=(m1+m2)/2

print("average of best two results :",avg)