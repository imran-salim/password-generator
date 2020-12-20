from random import SystemRandom
import string
import sys

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
        rand = SystemRandom()

        selected_chars = []
        for n in range(pw_len):
            rand_index = rand.randrange(len(random_chars))
            selected_chars.append(random_chars[rand_index])
        generated_pw = ''.join(selected_chars)

        print('\nHere is your randomly generated password of your specified length of ' + str(pw_len) + ':\n' + generated_pw)
        terminated = True
    except:
        print('\nInvalid input was entered. Please provide a number in between 8 and 80 inclusive.')
        terminated = True