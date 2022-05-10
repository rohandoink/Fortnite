# Methods are blocks of code that are executed with a command
# Methods can be called anything, except keywords
# Predefined Python methods
# Methods are created at top of program in Python
# Use the keyboard "def" before the method

# Method definition
# This method does not have any parameters
def foo():
    # code to be executed when method is called
    print("Hello World!")

    
# This method takes 2 parameters
def bar(x,y):
    sum = x + y
    return sum 
    
variable = bar(7, 3)

print(variable)