import this
import antigravity

# the walrus operator

def func(x):
    # does some long computation
    return x + 1
# the code listed below is not efficiently written
if func(4) >= 5:
    print(func(4))

# use walrus operator instead
if (x := func(4)) >= 5:
    print(x)
# needs to be in (), otherwise it will evaluate incorrectly
# also, cannot use outside of a statement.


# the mutability of objects

a = "".join(["o","k"])
b = "o" + "k"
c = "ok"
print(a is b)
print(a is c)
print(b is c)
# this will print True True False.
# this is due to Interning, method of storing only 1 copy
# of each string value, which must be immutable (no change possible over time)
# because we used the .join method, compiler does not know that it will equal "ok"
# .join method is interpreted and run at run time, not compile time

# is operator is not the same as ==.
# == compairs the equivalence of objects
# example: d, e = [], []
# print (d == e) would eval to true, since they are both empty lists
# print (d is e) would eval to false, since they are not the same empty list
# checks mem address location.


# Chained operations
print((1 == 1) in [1])
print(1 == (1 in [1]))
print(1 < (0 < 1))
print(1 < 0 < 1)

# prints True True False False
# True == 1 in Python, example print(True == 1) returns True
# print(True + 1) would return a value of 2, because True = 1.
# for print(1 < (0 < 1)), 0 is less than 1, so that gives us True
# True is not less than 1, it is 1. so the third statement will be False
# False = 0. The 4th statement is actually being evaluated
# 1 < 0 and 0 < 1, the first statement is False, so it returns as False overall


# Dictionary Key Hashing
d = {}
d[1] = 'hi'
d[1.0] = 'hello'
d[2 - 1] = 'yo'
# dictionary created, 3 keys created
print(d)
# prints {1: 'yo'}
# d[1] and d[1.0] are the exact same
# equivelent keys in Python hash to the same value
x = hash(1)
y = hash(2 - 1)
print(x == y)
# this returns True, equivalent values in Python hash to the same thing
# important to know in dictionaries, since you wouldn't want 2 distict keys
# to hash to the same thing

# the all() function
# tells you if all of the values are equal to True

print(all([1, 2, 3]))
# if you were to put a False in that list, it would return a False
# because there is a single False in the list
# nested lists cause issues, an empty nested list is equal to False
# If you were to have all([[[]]]), which is nested 2 times,
# it would return True. this is because the second list, [[]],
# is not technically empty, it has a an empty list embedded in it.


# not
x = True
y = False
print(not x == y)
# This is True, not applies to x, so not True is False
# False == False, so this will print True
print(x == not y)
# this produces a syntax error. not has a lower importance than ==
# tries to evaluate the == before the not.
# print(x == (not y)) would work, because (not y) gets evaluated first

a, b = a[b] = {}, 5     # {} is dictionary
print(a, b)
# result is {5: {...}, 5)} 5
# 5 is holding a tuple. inside the tuple, it holds the dictionary
# {...} is a self holding dictionary. if this were to actually print,
# it would print infinitely, circular reference
# evals from left to right. first, a = {} and b = 5
# next, a[b] = {}, 5. {} is already assigned to a
# a at key b is equal to dictionary, 5
# this is what causes the circular reference




