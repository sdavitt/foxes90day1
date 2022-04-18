
def hello_name(user_name):
    print('Hello ' + user_name.upper() + '!')

# make a function do something by CALLING that function
# function_name(<parameters/arguments/inputs>)
hello_name('Carlos')
hello_name('Alex')
hello_name('Javie')

# string concatenation - taking multiple strings and adding them together to be one large string
a = 'Cat'
b = 'Dog'
c = a + b
print(c)

# f-string formatted string
def hello_name2(name):
    print(f'Hello {name.upper()}!')

hello_name2('Kristen')
hello_name2('Max')

# Don't use these as variable names: print, str, int, float, list, len, count, sorted
from random import randint
for number in range(1, randint(0, 100), 2):
    print(f'The current number is {number}.')


# Return max number from a list
my_list = [1, 2, 65, 3, 25, 33, 87, 32, -140]
# max does not print a value -> it returns a value
# the output of a function is its return value
# after execution, the function call will transform into the return value
#print(max(my_list)) # print the return value of the max function where my_list is the parameter for max
my_maximum = max(my_list)
#print(my_maximum)

# let's write our own version
# my max function
# input: a list of numbers
# output: the largest number from that list
# I need a way to compare all the values in my list to eachother
# Compare the values in the list inidividually to eachother
# and keep track of the maximum value we've seen so far
# We need to loop through the list tracking our max value
# and then return the max value after the loop
def my_max(nums):
    current_max = nums[0]
    for number in nums:
        if number > current_max:
            current_max = number
    return current_max

print(my_max([-10, -50, -2, -101]))

print('\n\n')
# the left and right sides of and/or must be complete conditionals
x = 7
if x%5 == 0 or x%10 == 0:
    print('Hello')

# conditional structure inside a return (just a bonus, you should use normal conditionals as you learn)
def leap_year(year):
    return f'{year} is a leap year!' if year%400 == 0 or (year%4==0 and year%100!=0) else f'{year} is not a leap year.'

print(leap_year(2020))
print(leap_year(2021))

# Hey look, a bunch of changes!
dog = 'Sir Henry James of Pailey'
print(dog)