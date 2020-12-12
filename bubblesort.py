'''
Insert 3 scrambled floats or integers and 
get them sorted in ascending order where 
x < y < z
'''

x = input("Insert first number")
y = input("Insert second number")
z = input("Insert third number")

temporary_var = max(x,y)
x = min(x,y)
y = temporary_var

temporary_var = max(y,z)
y = min(y,z)
z = temporary_var

temporary_var = max(x,y)
x = min(x,y)                   # A re-sort of x and y in the case where y < x
y = temporary_var

print(x)
print(y)
print(z)

# Because the variables are being constantly re-assigned, the temporary variable is a must
