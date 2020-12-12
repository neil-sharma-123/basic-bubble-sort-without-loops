'''
Insert 3 scrambled floats or integers and 
get them sorted in ascending order where 
x < y < z
'''

x = input("Insert first number")
y = input("Insert second number")
z = input("Insert third number")

x = min(x,y)
y = max(x,y)

y = min(y,z)
z = max(y,z)

x = min(x,y)    # A re-sort of x and y in the case where y < x
y = max(x,y)

print(x)
print(y)
print(z)

