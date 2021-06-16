import random

def getAnswer(answerNumber): #getAnswer function defined
    if answerNumber == 1:
        return 'Yes'
    elif answerNumber == 2:
        return 'eh, maybe'
    elif answerNumber == 3:
        return 'No way'

r = random.randint(1,3) #random.randint function called, w/ 2 arguments. This variable gets stored in r.
fortune = getAnswer(r) #getAnswer is called, with r as it's argument, program execution moves to the top of getAnswer() function.
# returned string gets assigned to variable named fortune
print(fortune)

#you can pass return values as arguements to another funtion call, so the above an be written instead as:
print(getAnswer(random.randint(1,3)))
#obviously, running this will produce 2 answers.




