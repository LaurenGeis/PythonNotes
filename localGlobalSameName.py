def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs) #prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) #prints 'global'
