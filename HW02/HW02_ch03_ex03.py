#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

#print('+', end=' ')
#print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


def print_four_dashes():
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')

def print_three_pipes():
    print('|', end='         ')
    print('|', end='         ')
    print('|', end='         ')

def print_3pipes_4times(func):
    func()
    print()
    func()
    print()
    func()
    print()
    func()
    print()

def print_plus_minus_line(func):
    
    print('+', end=' ')
    print_four_dashes() #4x
    print('+', end=' ')
    print_four_dashes() #4x
    print('+', end=' ')
    print()

print_plus_minus_line(print_four_dashes)

print_3pipes_4times(print_three_pipes)

print_plus_minus_line(print_four_dashes)

print_3pipes_4times(print_three_pipes)

print_plus_minus_line(print_four_dashes)




# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    



if __name__ == "__main__":
    main()
