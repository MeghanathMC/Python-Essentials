# d=[1,2,4.56,'megha',True]
# for i in d:
#     print(i)
# print(d[-1])
# print(d[0])
# d.append(False)
# print(d)
# d.insert(3,"Reddy")
# print(d)
# # d.remove("megha")
# # # print(d)
# # d.insert(3,1)
# # print(d)
# # c=d.count(True)
# # d.pop(True)
# print(type(d))
#
# d[5]="Meghanath Reddy MC"
# print(d)
# print(d[0:6:2])  #start:end:skip
#
# p=[79,'mani',False]
# d.extend(p)
# print(d)
# d[8]="kishore" #lists are mutable
# print(d)
a=[10,20,30,40,50]
a.insert(2,444)#insert an element at the specific index in the list
print(a)
a.pop(1)#specifiy index in the pop function will pop that element from the list
a.pop()#pop always pop last element from the list
print(a)
a.remove(444) #this will remove the particular element from the list
print(a)
a.reverse()#this will reverse the normal list
print(a)
print(a*2) #two times print same list
ch=['a','b','c','d']
a.extend(ch) #[ch] list is added to list [a]
print(a)