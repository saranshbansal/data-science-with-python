# what will be the output?

n = [1, 2, 3, 4, 5, 10, 3, 100, 9, 24]

n1 = [i for i in n if i > 5]

for e in n:
    print('inter-> ')
    if e < 5:
        print('removing: {}'.format(e))
        n.remove(e)
        print('list after removal: {}'.format(n))

print(n)
print(n1)
