# https://www.w3schools.com/python/python_for_loops.asp

# Write a program that asks the user for a positive integer n.
# Using a for loop and range(), print all positive integers greater than 0 and smaller than n.
#
# Sample output:
# Upper limit: 5
# 1
# 2
# 3
# 4

# Write your code here:

int = int(input("Type positive integer: "))
numbers = range(1,int)
for x in numbers:
    print(x)
