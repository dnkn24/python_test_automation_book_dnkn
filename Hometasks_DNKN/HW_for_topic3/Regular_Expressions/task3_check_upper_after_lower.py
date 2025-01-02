'''
Define if the string contains at least one Upper case letter followed by Lower case letters.
E.g. '75serS3' - False; '75WseTrS3' - True;
'''

import re

def check_required_characters(input_string):
    result = re.search(r'[A-Z][a-z]+', input_string) is not None
    if result is True:
        print(f" There are Upper case letters followed by Lower case letters present in the input string '{input_string}'")
    else:
        print(f"There are NO Upper case letters followed by Lower case letters present in the input string '{input_string}'")

while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        input_string =input(f"Input string: ")
        check_required_characters(input_string)
    else:
        print(f"D'oh, you've stopped the check!")
        break