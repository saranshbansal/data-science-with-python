# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship with condition in predicate expression
new_fellowship = [member for member in fellowship if (len(member) >= 7)]

# Create list comprehension: new_fellowship with condition in predicate expression
new_fellowship_1 = [member if (len(member) >= 7) else '' for member in fellowship]

# Print the new list
print(new_fellowship)

# Print the new list
print(new_fellowship_1)
