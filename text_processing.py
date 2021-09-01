"""
Program #: Progamming Project 4A
Programmer: Justin Zhou
Due: 07/19/2021
CS 3A, Summer 2021
Description: (This assignment provides practice in defining and using functions. We would like to demonstrate our ability to control strings and use functions.)
"""
def get_key_character():
    char = input('Please enter a SINGLE character to act as key:')
    while not(len(char) == 1):
      char = input('Please enter a SINGLE character to act as key:')
    return char

def get_string():
    strn = input('Please enter a phrase or sentence >= 4 and <= 500 characters:')
    while not(len(strn) >= 4 and len(strn) <= 500):
        strn = input('Please enter a phrase or sentence >= 4 and <= 500 characters:')
    return strn

def mask_character(the_string, key_character):
    strn = ""
    for i in the_string:
        if i == key_character:
            strn += '*'
        else:
            strn += i
    print('\n', strn)

def remove_character(the_string, key_character):
    strn = ""
    for i in the_string:
        if i == key_character:
            strn += ''
        else:
            strn += i
    print('\n', strn)

def countKey(the_string, key_character):
    count = 0
    for i in the_string:
        if i == key_character:
            count += 1
        else: count += 0
    print('\n# of occurrences of key character, ' + key_character + '; ' + str(count))


key_char = get_key_character()
the_str = get_string()
mask_character(the_str, key_char)
remove_character(the_str, key_char)
countKey(the_str, key_char)

""" ------------------- Sample Run --------------------
Please enter a SINGLE character to act as key:sdfs
Please enter a SINGLE character to act as key:
Please enter a SINGLE character to act as key:d
Please enter a phrase or sentence >= 4 and <= 500 characters:
Please enter a phrase or sentence >= 4 and <= 500 characters:''
Please enter a phrase or sentence >= 4 and <= 500 characters:at
Please enter a phrase or sentence >= 4 and <= 500 characters:sdf sdaf ASDF ASDFsdf sdf (*j ljsdf

s*f s*af ASDF ASDFs*f s*f (*j ljs*f

sf saf ASDF ASDFsf sf (*j ljsf

# of occurrences of key character, d; 5
---------------------- End Sample Run ----------------"""