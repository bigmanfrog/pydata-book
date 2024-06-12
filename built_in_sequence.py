#enumerate allows for a collection to be iterated over 
#and allows access to the value and index

the_collection = [1, 2, 3, 4, 5]
for index, value in enumerate(the_collection):
    print(f'index is: {index} and value is: {value}.')

#zip pairs up one sequence with another sequence.
#creates a list of paired tuples
##to see contents use list()
seq_1 = ["foo", "bar", "baz"]
seq_2 = ["one", "two", "three"]
seq_3 = [1, 2, 3]
zipped = zip(seq_1, seq_2, seq_3)

print(list(zipped))


#use enumerate() and f-string to output collection with index
for index, value in enumerate(the_collection):
    print(f'the index is: {index} and the value is: {value}')


#use sorted() to return a sorted list
the_list = [7, 1, 2, 5, 8, 9, 3]
the_sorted_list = sorted(the_list)
print(the_sorted_list)

#use zip() and list() to return a list of tuples with matching elements
##in multiple sequences
###zip() will create a zip object.  passing the zip object to list() will
###create a list of tuples of associated sequences.
seq_1 = ["foo", "bar", "baz"]
seq_2 = ["one", "two", "three"]
seq_3 = [1, 2, 3]
zipped_elements = zip(seq_1, seq_2, seq_3)
print(zipped_elements)
print(list(zipped_elements))

#reversed() will be an iteration in reversed order
##range(10) creates a range object [0,10)
##list() tranforms a sequence into a list object
reversed_list = list(reversed(range(10)))
print(reversed_list)

#List Comprehension
##Creates a new list from a collection using a conditional
### [<exp> for value in <collection> if <condition>]
### equivalent to
### result = []
### for value in collection:
###     if <condition>:
###         result.append(expr)

the_collection = [1, 2, 3, 4, 5, 6, 7, 8]
the_comprehension = [the_collection*2]

the_even_comprehension = [x^2 for x in the_collection if x % 2 == 0]
print(the_even_comprehension)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
#map can be used to map a function to each element in a
##collection
##so, for the len function and strings collection:
##
mapped_set = set(map(len, strings))
print(mapped_set)

##dict comprehension can be created with key: value pairs
##as the expression
dict_comp = {index: value for index, value in enumerate(strings)}
print(dict_comp)

#count used to count occurances of strings in strings
#extend used to add elements of one list to another
all_names = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
names_of_interest = []
for names in all_names:
    enough_a = [name for name in names if name.count('a') >= 2]
    names_of_interest.extend(enough_a)
print(names_of_interest)

##simplify the above for loop using a list comprehension only
the_names = [name for names in all_names for name in names if name.count('a') >= 2]
print(the_names)

#A list of tuples can be flattened with a simple comprehension
list_tup = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened_tup = [x for tup in list_tup for x in tup]
print(flattened_tup)