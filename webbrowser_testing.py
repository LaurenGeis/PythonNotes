import webbrowser, sys, pyperclip
webbrowser.open('https://inventwithpython.com')
# webbrowser can really only open URL's.
# useful if you use it to open something copied to clipboard

#! python3
# mapIt.py - Launches a map in the browser using an address
# from the command line or clipboard

if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
# TODO: Get address from the clipboard
else:
    # Get Address from clipboard
    # for this exercise, that is all I am doing
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)


