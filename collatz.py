def collatz(number):
    while number > 1:
        if number%2 == 0:
            number = number//2
            print(number)
            #return number
        else:
            number = number * 3 + 1
            print(number)
            #return number
try:
    print('Enter an integer:')
    number = int(input())

    collatz(number)
except ValueError:
    print('Please enter an integer')


'''
This was a nice project
I initially had the while outside the function
but I couldn't get it to work right
I should also wrap this in a try...
'''