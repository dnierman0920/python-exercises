# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
def letter_count(letter, string):
    dd = {} # create an empty dict
    for char in string: # iterate through each char in the string
        if char in dd: # if the same char has already been iterated over add 1 to the count
            dd[char] += 1
        else: # if the char has NOT been iterated over, add it to the dict and give it the value of 1
            dd[char] = 1
    return dd

print(letter_count('d', 'the dog days are over'))

#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.

#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}
