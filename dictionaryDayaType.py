#a dictionary is a mutable collection of many values
# indexes for dictionaries are called keys, a key w/ it's associated values is a key-value pair
# dictionaries are typed with braces {}
my_Cat = {'size':'fat', 'color':'grey', 'disposition':'loud'}
# assigns a dictionary to the my_Cat variable
# keys are size, color and disposition
print(my_Cat['size'])
#prints 'fat'

#unlike lists, items in dictionaries are unordered
#calling a key that does not exist in the dictionary will result in an error

birthdays = {'Dana':'10/11', 'Lauren':'02/06', 'Luke':'02/05'}
while True:
    print('Enter a name: (Or blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name]= bday
        print('Birthday database updated')
    #Data entered in is forgotten when the program terminates

#keys(), values() and items() methods
spam = {'color':'red', 'age':'42'}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

# the get() method
picnic_Items = {'apples':5, 'cups': 10, 'sandwiches': 6}
print('I am bringing ' + str(picnic_Items.get('cups', 0)) + ' cups')
print('I am bringing ' + str(picnic_Items.get('eggs', 0)) + ' eggs')
# no eggs in the list, so none get returned
