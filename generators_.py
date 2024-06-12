#Generators construct a new iterable object.
##normal functions have a return statement
##generators have a yield statement.
##normal functions return one object
##generators can return a sequence of multiple values.
def squares(n=10):
    #function will 
    print(f'generting squares from 1 to {n ** 2}')
    for i in range(1, n + 1):
        yield i ** 2

#no code is immediately executed from the below.
#basically just creates a generator object
gen = squares()
print(gen)

#Code is executed when elements are specifically requested
#from the generator.
#generators produce output of one element at a time, so 
#can result in using less memory
for x in gen:
    print(x, end=' ')



#Note that an iterator is an object that will return
##objects when used in a for loop.

#A generator constructs a new iterable object.
##this is convenient when multiple results need to be returned.
#generator expressions can also be created using parenthesis ()
#Generators are very similar to functions and are created
##in the same way with the exception that a 'yield' is used instead of a 'return'

#Generator comprehensions is used as a shorthand for generator functions:

##Generator comprehension are done with ( for x in iterable):
gen = (x**2 for x in range(100))

##the above generator expression is the shorthand for:
def _make_gen():
    for x in range(100):
        yield x ** 2

##when I see yield, it should associate generator
##so is useful when multiple iterable values are needed.
gen = _make_gen() #set variable gen = yield of _make_gen()

#itertools is a module that is useful for working with iterators
import itertools
def first_letter(x):
    return x[0]
names_list = ['Alan', 'Adam', 'Wes', 'Will', 'Zill', 'Yang']

for letter, names in itertools.groupby(names_list, first_letter):
    print(letter, list(names)) #name_list here is the resultant generator.  Applying list() displays in a list
