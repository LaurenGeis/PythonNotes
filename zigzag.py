import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # if the indent is increasing or not

try:
    while True: # this is the main program loop
        print(' ' * indent, end='')
        print('******')
        time.sleep(0.1) # Pauses for 1/10 of a second

        if indentIncreasing:
            indent = indent + 1 #increase the number of spaces
            if indent == 20:
                indentIncreasing = False # Changes the direction
        else:
            indent = indent - 1 # Decreases the number of spaces
            if indent == 0:
                indentIncreasing = True # Changes direction
except KeyboardInterrupt:
    sys.exit()