from os import urandom
from struct import unpack
import string

terminated = False
while not terminated:
    try:
        pw_len = int(input('Please specify a length between 8 and 80 inclusive for your desired password.\n\n'))

        if pw_len < 8 or pw_len > 80:
            print('\nThe length provided is not in between 8 and 80 inclusive.')
            terminated = True
            continue

        punctuation = string.punctuation
        letters = string.ascii_letters
        digits = string.digits
        random_chars = punctuation + letters + digits

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