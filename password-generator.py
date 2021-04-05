import secrets
from string import punctuation
from string import ascii_letters
from string import digits

terminated = False
while not terminated:
    try:
        pw_len = int(input('Please specify a length between 8 and 80 inclusive for your desired password.\n\n'))

        # Terminate the program if the password length provided is not between 8 and 80 inclusive
        if pw_len < 8 or pw_len > 80:
            print('\nThe length provided is not in between 8 and 80 inclusive.')
            terminated = True
            continue

        # Make a string of all possible valid password characters
        chars = punctuation + ascii_letters + digits

        # Generate a random password of the given length
        password = ''.join(secrets.choice(chars) for i in range(pw_len))

        print('\nHere is your randomly generated password of your specified length of ' + str(pw_len) + ':\n\n' + password)
        terminated = True
    except:
        print('\nInvalid input was entered. Please provide a number in between 8 and 80 inclusive.')
        terminated = True