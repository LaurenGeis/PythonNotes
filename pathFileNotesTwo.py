from pathlib import Path

# glob() returns a generator object
p = Path('C:\Program Files (x86)\Call of Duty Modern Warfare')
print(p.glob('*'))
print(list(p.glob('*'))) # returns generator of all files in p
# this is for getting file types, ex: list(p.glob('*.txt'))

# exists(), to determine if a path exists.
d_drive = Path('D:/')
print(d_drive.exists())

# writing to files
p = Path('spam.txt') # method call to create spam.txt
p.write_text('Hello') # writing to the file
print(p.read_text())

# open a file with the open() function
# read contents of a file w/ read()

# saving variables with the shelve module
import shelve
shelf_file = shelve.open('mydata')
cats = ['Tony', 'WK', 'TK']
shelf_file['Cats'] = cats
shelf_file.close()

shelf_file = shelve.open('mydata')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))

