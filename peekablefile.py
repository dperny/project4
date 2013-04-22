"""This module provides a file that supports peeking at the next character."""


class PeekableFile:
    """A file that supports peeking.

    The peek method is useful when you want to make a decision based on the next
    character in the file without consuming the character.

    Fields:
        -f: An open file.
    """

    def __init__(self, filename, mode='r'):
        self._f = open(filename, mode)

    def close(self):
        self._f.close()

    def peek(self, n):
        """Reads the next n characters in the file without consuming them.

        Reads characters from the file and then puts them back.

        Returns:
            A string of length n.
        """
        position = self._f.tell()
        s = self._f.read(n)
        self._f.seek(position)
        return s

    def read(self, n):
        return self._f.read(n)
