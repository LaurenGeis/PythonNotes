import re

#creating regex objects

phone_Number_Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #the compile() method
# \d is a digit character, phone_Number_Regex variable now contains a Regex object
#desired pattern gets passed into re.compile(), results get stored in the phone_Number_Regex variable
#the search() method
mo = phone_Number_Regex.search('My number is 490-445-7654')
print('Phone number found: ' + mo.group())

#regex grouping
#adding parenthesis will add groups in the regex:
phone_Number_Regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_Number_Regex.search('My number is 490-445-7654')
print(mo.group(1)) #will print first () group
print(mo.group(2))# will print second () group
print(mo.group(0))# will print all
print(mo.group())# will print all
print(mo.groups()) #plural groups would print everything

area_Code, main_Number = mo.groups() #mo.groups would return a tuple
print(area_Code)
print(main_Number)
