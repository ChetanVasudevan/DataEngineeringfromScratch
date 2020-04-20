#decorator function

#what are decorators ? Decorators are callable objects which are used to modify functions or classes.

#what are callable objects ? Callable objects are objects which accepts some arguments and returns some objects. functions and classes are examples of callable objects in Python. 

#example of a decorator function 

def decorator_func(some_func):
  # define another wrapper function which modifies some_func
  def wrapper_func():
    print("Wrapper function started")
    
    some_func()
    
    print("Wrapper function ended")
    
  return wrapper_func # Wrapper function add something to the passed function and decorator returns the wrapper function
    
def say_hello():
  print ("Hello")

#declaring a decorator_func to a variable, in my case i give it to say_hello  
say_hello = decorator_func(say_hello)


say_hello()


#Output
Wrapper function started
Hello
Wrapper function ended

#simple idea to remember: a decorator function is a function which accepts some other function as an input/argument.It defines a wrapper_func which calls some_func but it also executes some code of it’s own.
