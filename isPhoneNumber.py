def isPhoneNumber(text): # this is the created isPhoneNumber function.
    if len(text) != 12: #checks for a standard phone number lenght of 12 (including -'s)
        return False
    for i in range (0,3): #checks range 0-3
        if not text[i].isdecimal():
            return False
    if text[3]!= '-': #character 3 would have to be a - in a phone number
        return False
    for i in range (4,7): #checks range 4-7
        if not text[i].isdecimal():
            return False
    if text[7] != '-': #character 7 would have to be a - in a phone number
        return False
    for i in range(8,12): #checks range 8-12
        if not text[i].isdecimal():
            return False
    return True
print('Is 415-555-4242 a real number?')
print(isPhoneNumber('415-555-4242'))
print('is sdjklfkdsjlksj a phone number?')
print(isPhoneNumber('sdjklfkdsjlksj'))
print('is 1111111111 a real phone number?')
print(isPhoneNumber('1111111111'))

message = 'Call me at 455-455-4455 tomorrow. 415-415-7788 is my office number'
for i in range(len(message)):
    chunk = message[i:i+12] # on each iteration of the for loop, 12 characters from message is assigned to chunk
    if isPhoneNumber(chunk): #chunk gets passed into isPhoneNumber to see if it matches the phone number pattern. If it does, chunk gets printed.
        print('Phone number found: ' + chunk)