#Error Handling is all about handling potential errors gracefully.
##To make this work a try: except: is attempted.

#float will return the return value from float(x) when parameter x is valid.
##if the return value is not valid, an ugly ValueError: is returned

def attempt_float(x): #new function with x as parameter
#This is the generalized design where all error types
    try:
        return float(x)
    except:
        return x
#if the object cannot be made into a float, then the object will be returned
print(attempt_float('1.2'))
print(attempt_float('what?'))
print(attempt_float((1, 2)))

def attempt_float_type_error(x):
    try:
        return float(x)
    except ValueError:
        return x
    except TypeError:
        return f'{x} is not of a valid data type'
print(attempt_float_type_error((1, 2))) #pass a tuple type to function
print(attempt_float_type_error('testing string'))

#multiple types of errors can be given in a tuple
def attempt_float_type_error(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return f'{x} is not of a valid data type or value'
    
        
def attempt_float_finally(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return f'{x} is not of a valid data type or value'
    finally:
        print('this always will run')

print(attempt_float_finally('1.2'))