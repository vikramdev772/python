""" Set comprehensions in Python are a concise way to create sets.
 They have a similar syntax to list comprehensions but use curly braces {}
   instead of square brackets []. The basic structure is:

   
    {expression for item in iterable}

   
"""

# expression: This is the value you want to include in the set. It can be derived from the item in the iterable.

# item: This is the variable that takes on each value in the iterable.

# iterable: This is the sequence of values that the item variable takes on.

# Using a set comprehension to create a set of squares
squares = {x*x for x in range(1, 6)}
print(squares)

# {1, 4, 9, 16, 25}

# Using a set comprehension to create a set of odd numbers
numbers = {x for x in range(1, 11) if x % 2 != 0}
print("\n\t Set of odd num : ",numbers)
    # Set of odd num :  {1, 3, 5, 7, 9}



# Using a set comprehension to create a set of lengths of words
words = {"apple", "banana", "cherry"}
word_lengths = {len(word) for word in words}
print(word_lengths)
