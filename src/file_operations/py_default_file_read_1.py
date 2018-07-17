from env import path

# Open a file: file
file = open(path + 'moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

# Importing text file_operations line by line

# Read & print the first 3 lines
with open(path + 'moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())


