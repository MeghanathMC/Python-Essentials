#Datatypes
# 1)Numeric ->integer(3,4,6,7),float(3.14,5.7,8.7,4.67),complex(3+6j,-6+5j)
# 2)Boolean ->
# 3)sequence ->strings,list,tuple
# 4)dictionary
# 5)set
val=1
def func():
    val=50
    print("value of local varialbe= ",val)

func()
print("value of global varialbe : ",val)