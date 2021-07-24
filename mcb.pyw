#! python3
#mcb.pyw saves each piece of the clipboard text under a keyword.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keywords into clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard
import pyperclip, re, shelve, sys

mcb_shelf = shelve.open('mcb')

# TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # if the 1st cmd line argument is 'save',
    # the 2nd cmd line argument is the keyword for for the current content of the clipboard.
    # keyword is used as key for mcb_shelf, value is text currently on the clipboard.
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

# TODO: List keywords amd load content
if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcb_shelf.keys())))
elif sys.argv[1] in mcb_shelf:
    pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
