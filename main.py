from peekablefile import *
import sys
import string
from stack import LinkedListStack as stack
from typetoken import Typed_Token
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
    store = stack()
    while c:
        if c in string.digits:
            num = read_real(f)
            if isinstance(num,int):
                # print('Integer:',num)
                pass
            elif isinstance(num,float):
                # print('Float:',num)
                pass
        elif c == '<':
            f.read(1)
            c = f.peek(1)
            if c == '/':
                f.read(1)
                chars = read_string(f)
                c = f.peek(1)
                if c == '>':
                    try:
                        start = store.pop()
                    except IndexError:
                        # if there's nothing on the stack and we have an end tag, error and break
                        print("UnexpectedEndTagError: Unexpected </{0}> found!".format(chars))
                        return
                    # if the end tags doesn't match with the start, error out and break
                    if start.value != chars:
                        print("WrongEndTagError: Expected </{0}> but found </{1}>!".format(start.value,chars))
                        return
                    # print('EndTag:',chars)
                else:
                    # print('String:',chars)
                    pass
            else:
                chars = read_string(f)
                c = f.peek(1)
                if c == '>':
                    # this thing is a StartTag, put it on the stack
                    store.push(Typed_Token('StartTag',chars))
                    # print('StartTag:',chars)
                else:
                    pass
                    # print('String:',chars)
        elif c in string.ascii_letters:
            chars = read_string(f)
            # print('String:', chars)
        else:
            f.read(1) # discard the character
        c = f.peek(1)

    try:
        # grab anything left on the stack, if not empty it's an error
        end = store.pop()
        if end.kind == 'StartTag':
            print("MissingEndTagError: Expected </{0}> not found!".format(end.value))
        else:
            print("UnexpectedEndTagError: Unexpected </{0}> found!".format(end.value))

    except IndexError:
        #pass silently, nothing left in the stack
        pass


if __name__ == '__main__':
    main(sys.argv)
