# Create a list of strings: mutants
mutants = ['charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = enumerate(mutants)

# Print the list of tuples
print(list(mutant_list))

print('----------\n')

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

print('----------\n')

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
