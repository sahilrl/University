#! /usr/bin/python

# age = 27
# name = "Sarah"
# def birthday():
#     global age       # 'age' is in global namespace
#     age = 28
#     name = "Roark"
# birthday()
# print(age, name)

# -------------------------------------

# def countdown(start):
#     def display():
#         n = start
#         print(n)
#         return n
#     return display


# somefunc = countdown(5)
# print(somefunc)
# somefunc()



# -------------------------------------

# from urllib.request import urlopen
# def page(url): 
#   def get(): 
#     return urlopen(url).read() 
#   return get


# ''' In the above function page(), there is no computation yet. 
# It's just merely saving and returning the nested function get() 
# that could be executed later in program.
# '''
# url1 = page('http://google.com')
# url2 = page('http://villaforrest.ru')

# # print(url1())
# # print(url2())
# print(url1.__closure__)  # closure attribute tells if the function is closure or not.
#                          # Since url1 is closure it will the tuple of cell object
# print(page.__closure__) # Since page is not closure, it will return None

#The cell object has the attribute cell_contents which stores the closed value.

# print(url1.__closure__[0].cell_contents)
# print(url2.__closure__[0].cell_contents)

# -------------------------------------

# Closure in Python can be defined when a nested function references a value in its enclosing scope. Closures provide some form of data hiding. A closure can also be a highly efficient way to preserve state across a series of function calls. To create a closure function in Python:

#     We must have a nested function.
#     The nested function must refer to a value defined in the enclosing function.
#     The enclosing function must return the nested function.