#references

spam = 42 # assigning 42 to spam variable, creating 42 value and storing a reference to it in  the spam variable
cheese = spam # copying the reference
spam = 100 # creating a new value and storing reference to it in spam
print(spam)
print(cheese)

spam = [1, 2, 3, 4, 5]
cheese = spam #the reference is being copied, not the list
cheese[1] = 'hello' #this changes the list value
print(spam)
print(cheese)

#the id() function
id('howdy')
print(id('howdy')) #print the id of the stored string

#passing references
def eggs (some_Parameter):
    some_Parameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)
#spam and some_Parameter refer to the same list

#copy() ands deepcopy()
#copy.copy() can be used to make a duplicate copy of a mutable value.

import copy
spam = ['a', 'b', 'c', 'd']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) #cheese is a different list with a different identity
cheese[1] = 42
print(spam)
print(cheese)

