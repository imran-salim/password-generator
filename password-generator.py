from os import urandom
from struct import unpack
from string import punctuation as p
from string import ascii_letters as l
from string import digits as d

terminated = False
while not terminated:
    try:
        pw_len = int(input('Please specify a length between 8 and 80 inclusive for your desired password.\n\n'))

        # Terminate the program if the password length provided is not between 8 and 80 inclusive
        if pw_len < 8 or pw_len > 80:
            print('\nThe length provided is not in between 8 and 80 inclusive.')
            terminated = True
            continue

        # Collect a set of all possible valid password characters
        punctuation = p
        letters = l
        digits = d
        random_chars = punctuation + letters + digits

        # Generate a random password of the given length
        generated_pw = ''
        n = 0
        while n < pw_len:
            rand_c = unpack('c', urandom(1))[0]
            if rand_c in random_chars:
                generated_pw += rand_c
                n += 1

        print('\nHere is your randomly generated password of your specified length of ' + str(pw_len) + ':\n\n' + generated_pw)
        terminated = True
    except:
        print('\nInvalid input was entered. Please provide a number in between 8 and 80 inclusive.')
        terminated = True