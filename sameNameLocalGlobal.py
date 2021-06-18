def spam():
    global eggs
    eggs = 'spam' #this is the global
def bacon():
    eggs = 'bacon' #this is the local
def ham():
    print(eggs) #this is the global

eggs = 42 #this is the global
spam()
print(eggs)

#exception handling notes, handled by try block
def spam(divide_by):

    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Invalid argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#this will have the spam() call in the try block
def spam(divide_By):
    return 42 / divide_By
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Argument')