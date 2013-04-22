"""Example usage of the PeekableFile class."""


import string
from peekablefile import PeekableFile


def read_integer(f):
    digits = []
    c = f.peek(1)
    while c in string.digits:
        digits.append(f.read(1))
        c = f.peek(1)
    return ''.join(digits)


def read_string(f):
    chars = []
    c = f.peek(1)
    while (c in string.ascii_letters) or (c in string.digits):
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
            print('Integer:', read_integer(f))
        elif c in string.ascii_letters:
            print('String:', read_string(f))
        else:
            f.read(1) # discard the character
        c = f.peek(1)
    f.close()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
