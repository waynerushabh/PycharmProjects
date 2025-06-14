# Use of underscore to have ignored variable values

a=0
b=0

for _ in range(5):
    print(a)
    a+=1
    
    print(_)


# Note - _ can remain unused.