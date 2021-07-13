import pyinputplus as pyip
import time, random

number_of_questions = 8
correct_answers = 0

for question_number in range(number_of_questions): # program picks 2 numbers to multiply in for loop
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    prompt = '#%s: %s times %s = ' % (question_number, num_1, num_2)
try:
    # right answers are handled by allow_regexes
    # wrong answers are handled by block_regexes, w/ custom message
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num_1 * num_2)],
    blockRegexes=[('.*', 'Incorrect!')],
    timeout = 8, limit = 3) # timeout is 8 seconds, limit is 3 tries
except pyip.TimeoutException:
    print('Out of time!')
except pyip.RetryLimitException:
    print('Out of tries!')

else:
    # this block runs if no exceptions were raised by the try block
    print('Correct!')
    correct_answers += 1

    time.sleep(1) # 1 second pause to see answer.
print('Score: %s out of %s' % (correct_answers, number_of_questions))

# a few issues here, this does not keep a running tally, process finishes when answer is given.
# the number_of_questions variable is likely the cause,
# number_of_questions = 8, prints to screen: #7: 1 times 1, Score: 1 out of 8

