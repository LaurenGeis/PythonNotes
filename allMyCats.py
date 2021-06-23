catNames = [] # creates empty list
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list contactination
print('The cats names are: ')
for name in catNames:
    print(' ' +name)

#using a for loop to iterate over the indexes of a list
supplies = ['pens', 'books', 'staplers', 'brooms']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#in and not in operators
#used to determine if something is in or not in a list
'howdy' in ['hi', 'hello', 'hey', 'howdy']

#multiple assignements
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
#do this instead of size = cat[0]...
#needs to be exact match, otherwise it throws a ValueError

#the enumerate function
#enumerate() returns two values, index and item.
#useful if you need both the item and index in a loop's block
supplies = ['pens', 'books', 'staplers', 'brooms']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

#random.choice function
import random
pets = ['dog', 'cat', 'lizard']
random.choice(pets)
#entered into a interactive shell will give you a random item from the list.
#random.choice(someList) is just a shorter version of someList[random.randint(0, len(someList) - 1]

#random.shuffle(someList) , shuffles the order of the list.
pets = ['dog', 'cat', 'lizard']
random.shuffle(pets)
pets

