import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    if answer_number == 2:
        return 'It is decided'
    if answer_number == 3:
        return 'Yes'
    if answer_number == 4:
        return 'Try again'
    if answer_number == 5:
        return 'Ask later'
    if answer_number == 6:
        return 'Not looking good'
    if answer_number == 7:
        return 'No way'
    if answer_number == 8:
        return 'Maybe yes'
    
r = random.randint(1,8)
fortune = get_answer(r)
print(fortune)

'''
The get_answer function is called with 'r' as the argument.
Program execution moves to the top of the function.
The value of 'r' is stored as a parameter named answer_number.
Depending on the value in answer_number, the function returns only one string.
The returned string is assigned to a variable named 'fortune'.
This then gets passed to a print() call

It is possible to pass return values as an argument to another function call.
You could shorten the last 3 lines to:

print(get_answer(random.randint(1,9)))
'''