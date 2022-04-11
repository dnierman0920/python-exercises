# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there


def p_times(statement, number):
    for i in range(int(number)):
        print(statement)

some_number  = input('give me a number')

p_times('Hello there', some_number)

