#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        answer = a/b
        print(answer)
    except ZeroDivisionError as e:
        print(e)


def process_list(input_list):
    sum = 0
    for x in input_list:
        try:
            sum += int(x) ** 2
        except (TypeError, ValueError) as e:
            print(e)
    print(sum)

#TypeError
#ValueError
#sum of the squares of all integers in the list.



def nested_operations(a, b):
    try:
        intA = int(a)
        intB = int(b)
        try:
            divisionResult = intA / intB
            try:
                sqrt = divisionResult ** 0.5
                print(sqrt)
            except Exception as e:
                print(e)
                # sqrt imaginary error
        except Exception as e:
            print(e)
            # zero division error
    except Exception as e:
        print(e)
        # int conversion error

'''
convert both parameters to integers, divide the first by the second, and then calculate the square root of
the result. Use nested try-except blocks to handle potential ValueError (for conversion) and
ZeroDivisionError. If the final result is successful, return it; otherwise, return an appropriate error message.
'''

def process_input():
    '''
    Use a try block to convert the input to a float and calculate its square
    Use an except block to handle ValueError if the input is not a valid number
    Use an else block to print the result if successful
    Use a finally block to print "Processing complete"
    Return the result or None if an error occurred
    '''
    try:
        userIn = float(input("Enter a number: "))
    except ValueError as e:
        print("value Error")
        return None
    else:
        square = userIn ** 2
        return square
    finally:
        print("Processing complete")



