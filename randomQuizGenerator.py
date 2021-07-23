# skeleton script that contains quiz data
#! python 3
# randomQuizGenerator.py - creates quizzes with questions and answers in random order

import random

# quiz data. Keys are the states, values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut':'Hartford',
            'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
            }
for quiz_num in range(35): # making 35 separate quizzes

    # TODO: Create quiz with the answer key files.
    quiz_file = open(f'capitalsquiz{quiz_num +1}.txt', 'w') # the 'w' for opening in write
    answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w') # the 'w' for opening in write
    # answer key is stored in file capitals_answer<N>.txt
    # this will loop 35 times, first loop will create file
    # capitalsquiz1.txt and capitalsquiz_answers1.txt and so on.

    # TODO: Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n') # creates header for student to fill out
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')
    # the file names for the quizzes will be capitalsquiz<N>, where N is the
    # unique number for the quiz that comes from quiz_num.

    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states) # random.shuffle() reorders the values in any list passed in

    # TODO: Loop through all 50 states, making a question for each.
for question_num in range(50):
    # Get right and wrong answers, finds each state in capitals and stores corresponding state in correct_answer
    correct_answer = capitals[states[question_num]] # correct answer is stored in capitals dictionary
    wrong_answers = list(capitals.values()) # duplicates all values in capitals dictionary
    del wrong_answers[wrong_answers.index(correct_answer)] # deletes correct answer from above,
    wrong_answers = random.sample(wrong_answers, 3) # selects 3 random values from the list
    answer_options = wrong_answers + [correct_answer] # answers get randomized
    random.shuffle(answer_options)

    # TODO: Write the question and answer options to the quiz file
# write the question and the answer options to the quiz file
quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
for i in range (4):
    quiz_file.write(f"    {'ABCD'[i]}). { answer_options[i]}\n")
    quiz_file.write('\n')

    # TODO: Write the answer key to the file. 
answer_key_file.write(f"{question_num + 1}.{'ABCD'[answer_options.index(correct_answer)]}")
quiz_file.close()
answer_key_file.close()

# This actually didn't work. Creates .txt files but the questions and answers not appearing.


