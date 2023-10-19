import random
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key


def mergesort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[i]:
                lst[k]=left[i]
                i+=1
            else:
                lst[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            lst[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            lst[k]=right[j]
            j+=1
            k+=1
    return lst



my_list=[]
for i in range(10):
    my_list.append(random.randint(0,999))

print("unsorted list ")
print(my_list)
print("sorting using insertion sort")
insertionsort(my_list)
print(my_list)



my_list = []
for i in range(10):
    my_list.append(random.randint(0, 999))

print("unsorted list ")
print(my_list)
print("sorting using merge sort")
mergesort(my_list)
print(my_list)