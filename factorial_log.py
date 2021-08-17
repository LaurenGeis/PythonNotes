# when python logs an event, it creates a LogRecord
# object that holds the information about the event

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# this is what will print during log. The timestamp, DEBUG and message
logging.debug('Start of program')   # logging.debug() function used to print log information.
# debug() function calls basicConfig() and includes messages passed to debug()
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i  # i starts at 0.
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
        logging.debug('End of factorial(%s%%' % (n))
        return total
print(factorial(5))
logging.debug('End of program')

# i variable starts at zero, so this will show the wrong values for total
# changing the for statement to for i in range(1, n + 1) will start process at 1
# use logging.disable() a logging level, and it will disable notifications for that level
# ex: logging.disable(logging.CRITICAL)
