# escape characters
# use backslash \ followed by character to add in a string
# example: print('go to Dana's house) does not work, tries to create variables after 's house.
print('go to Dana\'s house')
# \n is for newline
print('Hello \nhow are you today? \nI am well')
#putting r in front of a string, this is a raw sting, prints all the text:
print(r'Hello \nhow are you today? \nI am well')
# you can achieve the new line effect w/ triple quotes as well
print('''Hello
How are you today?
I am doing well''')
# slicing strings by character position:
spam = 'hello world'
print(spam[0])
print(spam[1])
print(spam[-1])
print(spam[0:5])
fizz = spam[0:5]
print(fizz)

#boolean statements example
age = 18
old_enough_to_get_driving_licence = age >= 17
print(old_enough_to_get_driving_licence)

print('h' in 'hello')

#string interpolation

name = 'Lauren'
age = 10000
print('My name is %s and I am %s years old' %(name, age))
