#append() method. adds arguement to the end of a list.
spam = ['dog', 'cat', 'rat']
spam.append('moose')
print(spam)

#insert() method inserts ar desidnated space
spam.insert(1, 'chicken')
print(spam)

#methods belong to a single data type. something like:
# bacon = 42
#bacon.insert(1,'world') would not work.

#removing values
spam.remove('chicken')
print(spam)

#if a value appears multiple times on a list, it only removes the first instance.
#del is good if you know the index, remove works if you know the value.

#sort() method will sort a list of values
number_list = [10, 2, 8, 5, 3]
number_list.sort()
print(number_list)

#also does alphabetical sort,
#uses ASCIIbetical order, so any uppercase letters will go aead of lowercase, ex: Z before a
# pass in key=str.lower to sort in regular alphabetical order. causes sort() funtion to treat everything as lowercase
spam.sort()
print(spam)

#sorting in reverse order
spam.sort(reverse=True)
print(spam)



