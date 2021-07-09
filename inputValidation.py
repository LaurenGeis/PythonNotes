# an example of input validation

while True:
    print('Enter your age:')
    age = input()                                   # takes user input, assigns to variable age
    try:
        age = int(age)                              # looking for an integer for age
    except:                                         # except occurs if anything other than a positive or negative number is entered
        print('Please use numeric digits.')
        continue                                    #continues check
    if age < 1:
        print('Please enter a positive number ')
        continue
    break
print(f'Your age is {age}.')
