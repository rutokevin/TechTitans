#getting help
# help() in built function returns a function header and its argument, and what the function does briefly

# e.g 1
# help(round)

#returns ->
# Help on built-in function round in module builtins:

# round(number, ndigits=None)
#     Round a number to a given precision in decimal digits.
    
#     The return value is an integer if ndigits is omitted or None.  Otherwise
#     the return value has the same type as the number.  ndigits may be negative.

# help(round(-2.01)) # first calc the round arguments the help function explains what the function does

#e.g 2
# help(print)

#returns ->
# Help on built-in function print in module builtins:

# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
    
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.


#defining functions
#function is declared using def keyword name of function and () for parameter-argument and indented block of code after :
#thi function returns min of three differences btwn arguments passed
def least_difference(a,b,c): # passing parameters
    diff1=abs(a - b)
    diff2=abs(b - c)
    diff3=abs(a - c)
    return min(diff1,diff2,diff3) # returns min of absolute values of the differences
print(least_difference(-10,4,7)) # passing arguments -> a,b,c

print(# python allows trailing commas in argument list
    least_difference(1,10,100),
    least_difference(1,10,10),
    least_difference(5,6,7)
)#-> 9 0 1

# help(least_difference) # tells us what our function does
# Help on function least_difference in module __main__:

# least_difference(a, b, c)
#     defining functions
#     function is declared using def keyword name of function and () for parameter-argument and indented block of code after :
#     thi function returns min of three differences btwn arguments passed


#docstrings
#docstring is a tripple-quoted string(may span across multiple lines) that comes immediately after the header of a function.
def least_diff(a,b,c):
    """
    Returns the smallest difference between
    any two numbers
    >>> least_diff(1,5,-5)
    4
    """
    diff1=abs(a - b)
    diff2=abs(b - c)
    diff3=abs(a - c)
    return min(diff1,diff2,diff3)

# When we call help() on a func it shows docstring 
# help(least_diff)
# Help on function least_diff in module __main__:

# least_diff(a, b, c)
#     Returns the smallest difference between
#     any two numbers
#     >>> least_diff(1,5,-5)
#     4

#functions that do not return -> only called for side effects
def lt_diff(a,b,c):
    """
    Returns the smallest difference between
    any two numbers
    >>> least_diff(1,5,-5)
    4
    """
    diff1=abs(a - b)
    diff2=abs(b - c)
    diff3=abs(a - c)
    min(diff1,diff2,diff3)

print(# python allows trailing commas in argument list
   lt_diff(1,10,100),
   lt_diff(1,10,10),
   lt_diff(5,6,7)
)#-> None None None

mystery=print()
print(mystery) #-> None

# default arguments
#if we add sep the output is separated using the char
print(1,2,3, sep='-') #-> 1-2-3
#but if we dont include sept default value = ' '(optional argument)
print(1,2,3) #-> 1 2 3

def greet(who="colin"):
    print(f"Hello, {who}") #->Hello, colin
greet() #calling function with optional argument defaults to default value e.g colin
greet(who="Kaggle") #->Hello, Kaggle -> here we passed unambiguous argument
greet("world") #->Hello, world

#functions applied to other functions(higher order functions)
#supply functions as argument to other function
def mult_by_five(x):
    return 5 * x

def call(fn,arg):
    """
    call fn on arg
    """
    return fn(arg)

def squared_call(fn,arg):
    """
    call fn on the result of calling fn on arg
    """
    return fn(fn(arg))


print(
    call(mult_by_five,1),
    squared_call(mult_by_five,1),
    sep='\n' # '\n' its a newline char starts a newline
)# -> 5
 # -> 25

# another example of a higher order function
def mod_5(x):
    """
    returns the remainder of x after dividing by 5
    """
    return x % 5

print(
    'Which is biggest ?',
    max(100,51,14),
    'Which is biggest modulo ?',
    max(100,51,14, key=mod_5),
    sep='\n'
 ) #-> Which is biggest ?
   # 100

  #-> Which is biggest modulo ?
  # 14