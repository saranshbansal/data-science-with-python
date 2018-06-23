# An ITERABLE is:
#
# anything that can be looped over (i.e. you can loop over a string or file) or
# anything that can appear on the right-side of a for-loop:  for x in iterable: ... or
# anything you can call with iter() that will return an ITERATOR:  iter(obj) or
# an object that defines __iter__ that returns a fresh ITERATOR,
# or it may have a __getitem__ method suitable for indexed lookup.
#
# An ITERATOR is an object:
#
# with state that remembers where it is during iteration,
# with a __next__ method that:
# returns the next value in the iteration
# updates the state to point at the next value
# signals when it is done by raising StopIteration
# and that is self-iterable (meaning that it has an __iter__ method that returns self).
#
# Notes:
#
# The __next__ method in Python 3 is spelt next in Python 2, and
# The builtin function next() calls that method on the object passed to it.
#
# EXAMPLES ::

# s is a str object that is immutable
# s has no state
# s has a __getitem__() method
s = 'cat'      # s is an ITERABLE
print(next(s))  # TypeError: 'str' object is not an iterator

# t has state (it starts by pointing at the "c"
# t has a next() method and an __iter__() method
t = iter(s)    # t is an ITERATOR

next(t)        # the next() function returns the next value and advances the state
next(t)        # the next() function returns the next value and advances
next(t)        # the next() function returns the next value and advances
next(t)        # next() raises StopIteration to signal that iteration is complete

# >>> iter(t) is t   # the iterator is self-iterable
