#tuple is fixed-length; immutable when created
#created with parenthesis and commas
tup = (4,5,6)
#typically, tups are created using parentheses, but not necsarry; 
#tups can be created with just the commas
tup = 4,5,6
#any sequence or iterator can be converted to a tuple using tuple()
the_sequence = range(5)
the_tuple = tuple(the_sequence)
print(the_tuple)

the_iterator = iter('the string')
print(the_iterator)
print(next(the_iterator))
print(next(the_iterator))

#a For loop is a shortcut for creating an iterator object and executes next()
for obj in the_iterator:
    print(obj)

#mutable objects within a tuple can be modified in place
the_tup = tuple(['foo', [1, 2], True])
#in the above tuple() converts the list to a tuple.
#with object 0 a string, object 1 a list, and object 2 a Boolean
#a list is mutable, so can be changed in place; no new objects are created
#simple tuples can just use commas
#more complex tuples require the use of paretheses
nested_tup = 1,(2,3),(7,8),[1,2]
print(nested_tup)

#modifying mutable objects in tuples in place is possible
nested_tup[3].append(3)
print(nested_tup)

tup_1 = (4, None, 'foo')
tup_2 = (6,0)
tup_3 = ('bar',) #comma here is needed to create tuple
tup_cat = tup_1 + tup_2 + tup_3
print(tup_cat)

#multyplying tuples and lists will concatenate copies of the tuples or lists
print(('foo', 'bar')* 4)

#Tuples can be unpacked using tuple like expression of variables
tup = (4,5,6)
a, b, c = tup
print(c) #a=4, b=5, c=6

#sequeces with nested tuple can be unpacked
#using same structure-like expression
the_tup = 4, 5, (6, 7)
a, b, (c, d) = the_tup
print(d)

#iterate over sequence:
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f'a = {a}, b = {b}, c = {c}')

# *rest can be used to unpack the rest of a sequence into a list
# there will be a object called rest with a list of the remaining objects
the_sequence = [1,2,3,4,5,6,7,8,9]
a, b, *rest = the_sequence
print(a)
print(b)
print(rest)

#List
#lists are variable length; they are mutable.
# square brackets [] or list() can be used to create lists
#lists can take a generator function and materialize a list
mat_list = list(range(0, 10))
print(mat_list)

#append() can add elements to the end of a list
mat_list.append(10)
print(mat_list)

#insert() can be used to insert at a specific place in list
#but it is computationally expensive.
mat_list.insert(1,11)
print(mat_list)

#remove() is used to remove the FIRST occurance of parameter
b_list = list(('foo', 'red', 'baz', 'dwarf'))
b_list.append('foo')
print(b_list)
b_list.remove('foo')
print(b_list)

#in keyword returns boolean based on if value is in sequence
print('red' in b_list)

#not in keyword returns boolean based on if value is in sequence
print('red' not in b_list)

#lists can be concatenated with +
print([4, None, 'foo'] + [1,3,(3,4)])

#concatenation is expensive, so extend() is prefered 
list_of_lists = [[1, 2, 3], [4, 5, 6], [9, 8, 7]]
everything = []
for chunk in list_of_lists:
    everything.extend(chunk)

print(everything)

everything.sort()
print(everything)

#.sort() has a key parameter that allows a function to determine sort method
b = ['saw', 'saww', 'sa', 's']
b.sort(key= len) #note the name of the function is used without the parentheses
print(b)

# indexing operator is [], square brackets and uses [start:stop] for slicing
# the stop index is not included in the returned slice
seq = [7,2,3,7,5,6,0,1]
seq[1:2]
print(seq[1:2])
#slices can also take a step parameter to take every 2nd or 3rd or 4th value
print(seq[::2])

#a step of -1 can have the effect of reversing a list
print(seq[::-1])


#Dictionary
## typically represented as key : value pairs and created
## typically created with curly braces {}.

empty_dict = {}
d1 = {"a": 'some value',
      "b": [1, 2, 3, 4]
      }
print(d1)

#referencing a dict value is done with the key as index
print(d1['b'])

#checking to see if the key is in the dict can be
#done like checking if a value is in a list
print('b' in d1)

#del will just delete the key: value
#pop will delete the key: value and return the value
#you can add a new key: value using the d[index] = value
#syntax

d1[88]= 'new value'
print(d1[88])
d1[89]= 'another new value'

del d1[89]
print(d1[88])
return_value = d1.pop(88)
print(return_value)


#dict.keys() and dict.values() methods return an iterator
#iterator objects can be turned into lists.  the order
#returned will be the order that the key: value pairs
#were inserted into the dict

print(d1.keys())



#dict.items() will return a series of tuples as 
#(the key, the value)...

#dictionaries are mutable, so can be merged....in place.
##merging is done with dict.update()

d1.update({'c': 'irksome', 'd': 'quirksome'})
print(d1.items())


mapping = {}
key_list = [1,2,3,4,5]
value_list = ['one', 'two', 'three', 'four', 'five']
for key, value in zip(key_list, value_list):
    mapping[key] = value

print(mapping.items())

d1 = {'a': 'apple', 'b': 'batman'}
d2 = {'c': 'crab', 'd': 'data'}
print(type(d1))
print(d1.items())
d1.update(d2)
print(d1.items())

mapping = {} #empty dict
for key, value in zip(range(5), reversed(range(5))):
    mapping[key] = value
print(mapping.items())


tuples = zip(range(5), reversed(range(5)))
print(list(tuples))

#create a list with the first letter of each word being the dict key
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word] #new list is created
    else:
        by_letter[letter].append(word) #new word is added to list
print(by_letter)

#the above will return a dict type like:
#{'a': ['apple', 'aton'], 'b': ['bat', 'bar', 'book']}


words = ['apple', 'bat', 'bar', 'atom', 'book']

#need an empty dict
dict_by_a_z = {}
#iterate over the words
#A dictionary is created with the key being a letter and the associated object being a list
for word in words:
    #id first letter of each word
    letter = word[0]
    #if first key:
    if letter not in dict_by_a_z:
        dict_by_a_z[letter] = [word] #dict key is sliced by dict_name[key_value].  Lists are identified by [element_1, element_2, element...]
    #if key already exists, need to append to list
    else:
        #when indexing an object, use square [] brackets instead
        #of ().  I keep using () and debugging takes forever
        #because () looks like []
        dict_by_a_z[letter].append(word)

#dictionaries have a .setdefault(key, object).append(element) method
#which can be used to solve the above
##iterate over collection then use .setdefault().append()
dict_by_a_z = {}
for word in words:
    letter = word[0]
    #if the key does not exist, then there is a default object assigned.
    #else append object
    ##note that dictionary keys must be hashable (strings, float, int, tups of immutable objects)
    ##if there is an error, the default value will be:
    dict_by_a_z.setdefault(letter, []).append(word)
dict_by_a_z


#collections.defaultdict is a type that automatically deals with possible errors:
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

#the keys of a dictionary need to be hashable.
#hashability can be checked with hash():
hash('ahjahah')
#hash([1,2,3]) this will return an error because lists are
#not hashable.  Associate hashable with immutable.


#sets are unique, but unordered
##to ensure a collection in a list is unique, set() can be used
set([2,2,2,1,3,3]) #returns a set {2,1,3}

#curly braces are also used to signify sets
{1,1,2,2,3,4} #returns {1,2,3,4}; this is a set literal

#sets are useful for 'set operations' like union,
#intersection, difference.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
#union
a.union(b)
print(a | b)

#intersection
a.intersection(b)
print(a & b)

#all of the logical set operations have in-place counterparts.
#this is like saying 'a += b' which results in a being
#replaced by the sum of a and b.

print(a)
print(b)

a |= b
print(a)

c = b.copy
a &= c
print(a)


















