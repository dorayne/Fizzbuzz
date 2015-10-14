#!/usr/bin/env python

# initialize default values for variables
start_c = 1
end_d = 101
div_a = 3
div_b = 5

def error_check(test):
    # convert input to integer, exit program is input is not a number
    try:
        tested = int(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def fizzbuzz():
    # Fizzbuzz logic:
    # Print all num in seq,
    # replace with "fizz" if divisible by div_a,
    # with "buzz" if divisible by div_b
    # and with "fizzbuzz" if divisible by div_a AND div_b
    global div_a, div_b, seq
    for num in seq:
        if num % div_a == 0 and num % div_b == 0:
            print "fizzbuzz"
        elif num % div_a == 0:
            print "fizz"
        elif num % div_b == 0:
            print "buzz"
        else:
            print num

# Get user input
# run error_check if length of input is > 0
# variable will not be changed from default if input is <= 0
a = raw_input("Enter fizz divisor \n")
if len(a) > 0:
    div_a = error_check(a)

b = raw_input("Enter buzz divisor \n")
if len(b) > 0:
    div_b = error_check(b)

c = raw_input("Enter range start \n")
if len(c) > 0:
    start_c = error_check(c)

d = raw_input("Enter range end \n")
if len(d) > 0:
    end_d = error_check(d)

if start_c > end_d:
    seq = range(start_c, end_d + 1, -1)
elif start_c < end_d:
    seq = range(start_c, end_d + 1)
elif start_c == end_d:
    print "Cannot create range from 2 equal numbers, please try again"
    exit()
else:
    print "What did the math break?"

print "\n"
fizzbuzz()