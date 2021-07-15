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
print (21+int('5'))
# Global vs. local variables in functions
def stat():
    print('Hola amigos')
    a = 20
    print(a)
stat()
print(a)
b = 'sharf'
print(b)