import re

#functions are defined with parameters and 
##will optionally return a value typically based on passed in
##parameters
##if there is no return specified
##then the default return will be None
#below: x and y are positional arguments
# z is a keyword argument
def my_function(x, y, z=2):
    return x + y + z

result = my_function(2, 3)
print(result)

#a function will return a single object
##If multiple elements need to be returned
##the elements can be packed into a single tuple.
##then the tuple can be unpacked if needed where called


#placing function names in a list can be convenient
#for organization and allows a list of funtions to be
#used against a collection of values.  Kind of like map funtion
states = ['   Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrida', 'south carolina#', 'west Virginia?']

def remove_punctuation(value):
    return re.sub("!#?", "", value)

#list of cleaning functions:
clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

result = clean_strings(states, clean_ops)
print(result)


#Lamda Functions are also called anonymous functions
##Lambdas are single statement functions.

def apply_to_list(the_list, f):
    return [f(x) for x in the_list]

ints = [4, 0, 1, 5, 6]

result = apply_to_list(ints, lambda x: x * 2)
print(result)

#a lambda can be used as a key for sort function
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(x)))
print(strings)


#a lambda can be used as a one variable short function

short_function = lambda x: x**2 #the ** is raised to power
print(short_function(4))
