"""
The challenge: find the first non repeating character in a string


"""
s = "abacabad"


def firstNotRepeatingCharacter(s):
    for i in s:
        if s.index(i) == s.rindex(i):
            return i
    return '_'


