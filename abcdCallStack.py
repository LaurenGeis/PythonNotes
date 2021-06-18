def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c(): #c doesn't call anything, just displays c()
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
a() #when a() is called, it calls b(), which calls c().

def spam():
    eggs = 99 #second, local variables eggs is set to 99
    bacon() #third, bacon function is called. second local scope created.
    print (eggs)
def bacon():
    ham = 101 #local variable ham is set to 101, this is a new local scope.
    eggs = 0 #this is a new local variable.
    #print eggs() would print the local variable in bacon() call.
spam() #first, spam() gets called, local scope is created,
# when bacon() gets called, the local scope for that call is destroyed.
#local variables in one fucntion are completely seperate than those in another function.


