#!/usr/bin/python3

for char_code in range(ord('a'), ord('z') + 1):
    if (chr(char_code) != 'e' and chr(char_code) != 'q'):
        print("{}".format(chr(char_code)), end='')
