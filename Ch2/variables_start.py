# 
# Example file for variables
#

# Declare a variable and initialize it
a = 10
print(a)

# re-declaring the variable works
a = 'sharf'
print(a)

# ERROR: variables of different types cannot be combined
#a,b = 'sharf', 10
#c = a+b
#print(c)
# Global vs. local variables in functions
a = 10
def stat():
    print('Hola amigos')
    a = 20
    print(a)
stat()
print(a)