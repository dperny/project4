from peekablefile import *
import sys
import string
SPEC_CHARS = ['_']

def read_real(f):
    digits = []
    c = f.peek(1)
    while c in string.digits or c == ".":
        digits.append(f.read(1))
        c = f.peek(1)
    return eval(''.join(digits))

def read_string(f):
    chars = []
    c = f.peek(1)
    while (c in string.ascii_letters) or (c in string.digits) or (c == '_'):
        chars.append(f.read(1))
        c = f.peek(1)
    return ''.join(chars)

def main(argv):
    if len(argv) < 2:
        print('Usage: python3 peek.py FILE')
        return 1

    f = PeekableFile(argv[1])
    c = f.peek(1)
    while c:
        if c in string.digits:
            num = read_real(f)
            if isinstance(num,int):
                print('Integer:',num)
            elif isinstance(num,float):
                print('Float:',num)
        elif c == '<':
            f.read(1)
            c = f.peek(1)
            if c == '/':
                f.read(1)
                chars = read_string(f)
                c = f.peek(1)
                if c == '>':
                    print('EndTag:',chars)
                else:
                    print('String:',chars)
            else:
                chars = read_string(f)
                c = f.peek(1)
                if c == '>':
                    print('StartTag:',chars)
                else:
                    print('String:',chars)
        elif c in string.ascii_letters:
            chars = read_string(f)
            print('String:', chars)
        else:
            f.read(1) # discard the character
        c = f.peek(1)

if __name__ == '__main__':
    main(sys.argv)
