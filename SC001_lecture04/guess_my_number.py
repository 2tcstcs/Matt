"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
   print('Guess a number from 0-99:')
   while True:
       guess = int(input('guess a number:'))
       if guess > SECRET:
           print('too high')
       elif guess == SECRET:
           break
       else:
           print ('too low')
   print('congrates!')



"""
    print('guess a number from 0-99:')
    guess = int(input('Your guess:'))
    while guess != SECRET:
        if guess > SECRET:
            print('Too high')
        else:
            print('Too low')
        guess = int(input('Your guess:'))
    print('congrats number is:'+str(guess))
"""


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
