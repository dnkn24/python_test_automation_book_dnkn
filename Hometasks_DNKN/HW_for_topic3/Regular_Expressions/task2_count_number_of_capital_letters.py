'''
Count a number of Upper case letters in the string.
E.g. '7865serS3' - 'Number of Capital letters: 1'
'''

import re

def count_capitals(input_string):
    result = re.findall(r'[A-Z]',input_string)
    print(f"The number of Capital letter: {len(result)}")


while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        input_string =input(f"Input string: ")
        count_capitals(input_string)
    else:
        print(f"D'oh, you've stopped the check!")
        break

