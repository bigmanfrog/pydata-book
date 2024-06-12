#Set.Methods
##.add
### set.add(e) will add an element e to the set
set_a = {1, 2, 3}
print(set_a)
set_b = {4, 5, 6}
print(set_b)
set_add = set_a.add(7)
print(set_a)

#set.clear().  results in set(), which is an empty set.
set_a.clear()
print(set_a)

#set.remove(e). removes an element from set
set_a = {1, 2, 3}
set_a.remove(2)
print(set_a)

#set.pop().  removes arbitrary element; in Python removes first element
## returns removed element as well.

popped = set_a.pop()
print(popped)


#in-place set operations may be an efficient way to 
##work with multiple sets
set_a = {1, 2, 3}
set_b = {2, 3, 4, 5}

set_a |= set_b
print(set_a)

set_a = {1, 2, 3}
set_b = {2, 3, 4, 5}

set_a &= set_b
print(set_a)

#Elements of sets must mutable (in other words: hashable)
##therefore, if a set element is a list, it can be 
##converted to a tuple first.

the_data = [1, 2, 3, 4]
the_set = {tuple(the_data)} #a set must contain hashable elements, so a tuple is used here

#a set can be checked for being a subset

print({1, 2, 3}.issubset(the_set))

#a set can be checked for being a super-set
print({1, 2, 3}.issuperset({1, 2}))

#set equality can be checked
{1, 2, 3} == {2, 3, 1} #a set is equal to another set if all of the elements in one are the elements in the other.
