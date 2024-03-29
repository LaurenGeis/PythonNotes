# Raise statements consist of the raised keyword,
# a call to Exception() function and a string w/ error message

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print (symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) +symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4)), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exeption has occured: ' + str(err))