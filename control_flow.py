
#break can be used to exit out of the current loop of which the break
#keyword is a part of when condition is met
"""sequence = [1,2,0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value

print(total_until_5)
"""

"""
#range(a,b) will be a sequence of a to b, excluding b, but including a
thesequence = range(4)
print(thesequence)
for value in thesequence:
    print(value)

"""

"""
for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i,j))
"""

#While loops
#keeps executing a block until a condition is met


"""
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2

print(total)
"""

#pass is 'do nothing'; typically used as a placeholder
#for code to be filled in later

"""
if x < 0:
    print("negative!")
elif x == 0:
    #code to be input later
    pass
else: #else is catchall for all other situations
    print("positive")
"""

#range is used to create an evenly spaced sequence of 
#integers
##range(10) will create a sequence of [0,9] or [0,10) inclusive


#list() can be used to creat a list object from a sequence object
"""a_list = list(range(0,20,2))
print(a_list) 

for index in range(len(a_list)):
    print(f'element {index}: {a_list[index]}')
"""

#sum all numbers within a range of numbers that are
#divisible by 3 or 5 from [0,99999]
total = 0

for number in range(100000):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)

