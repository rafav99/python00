import sys

alphanum_morse = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'
}

if len(sys.argv) > 1:
    onearg = (' ').join(sys.argv[1:])
    strmay = onearg.upper()
    morse = ''
    for i in strmay:
        if i in alphanum_morse:
            morse = morse + alphanum_morse[i] + ' '
        elif i == ' ':
            morse = morse + '/ '
        else:
            print("ERROR")
            exit()
    print(morse)