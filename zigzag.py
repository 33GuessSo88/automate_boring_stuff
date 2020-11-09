import time
import sys

indent = 0 # how many spaces to indent
indent_increasing = True # whether the indentation is increasing or not

try:
    for i in range(1, 50): # the main program loop
        print(' '*indent, end='')
        print('**********')
        time.sleep(0.1) # pause for 0.1 seconds

        if indent_increasing:
            # increase the number of spaces
            indent = indent + 1
            if indent == 20:
                # change direction
                indent_increasing = False

        else:
            # decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # change direction
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()

'''
I had a ton of trouble with the indentation of the if and else.
I had it in line with the for
So the if would never fire
WATCH THE INDENTATIONS!!!!!

The try/except was if you change the for loop to a while loop
It was to demonstrate the ctrl C keyboard interrupt cleanly exiting without
a big error message
'''