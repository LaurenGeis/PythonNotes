#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(       # triple quoute syntax, creates multiline string. 
    (\d{3}|\(\d{3}\))?              # area code, \d to detect digits{3}, \ to escape the parenthesis, ? "for the optional" area code
    (\s|-|\.)?                      # separator, can be a \s for any space, tab or newline character, or a - or a . 
    (\d{3})                         # first 3 digits of the number
    (\s|-|\.)                       # separator again
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension, * matches zero or more of the preceding group. followed by 2-5 digits. ext is optional. 
    )''', re.VERBOSE)

#TODO : create email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username characters(a-z, A-Z, 0-9, dot, underscore,hyphen, percent, plus) +
    @                               # the @ symbol
    [a-zA-Z0-9.-]+                  # domain name characters(a-z, A-Z, 0-9, dot, hyphen)+
    (\.[a-zA-Z]{2,4})               # dot-something that is 2-4 characters in length
    )''', re.VERBOSE)
# email addresses have a lot of weird rules, so this won't catch everything, but will catch most standard emails

#TODO: Find Matches in clipboard text
#use pyperclip.paste() function.
#findall() regex method will return a list of tuples

text = str(pyperclip.paste())
matches = []                        # store matches in a list variable named matches
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # joining each number group
    if groups [8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])       # append groups 0 for email (group 0 matches the entire regex


#TODO: Copy Results to the clipboard

# pyperclip.copy() function will only takes a single string value.
# call the join() method on matches, since pyperclip.copy() only takes one string.

if len(matches) > 0:
    pyperclip.copy('\n'. join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')

