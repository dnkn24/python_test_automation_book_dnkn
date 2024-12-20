'''
Define if a string contains the required characters.
E.g. if '7865serS3' includes '583' - True; '973' - False
'''


import re

def check_required_characters(input_string, required_chars):
    pattern = ''.join(f'(?=.*{re.escape(char)})' for char in required_chars)
    result = re.search(pattern, input_string) is not None
    if result is True:
        print(f" Characters '{required_chars}' are present in the input string '{input_string}'")
    else:
        print(f"Characters '{required_chars}' are absent in the input string '{input_string}'")

while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        input_string =input(f"Input string: ")
        required_chars= input(f"Input required characters: ")
        print(check_required_characters(input_string, required_chars))
    else:
        print(f"D'oh, you've stopped the check!")
        break
