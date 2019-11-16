"""
The problem given an array "a" in which there are some unique as well as several duplicates print the first
appeared duplicate

Example: a = [2, 1, 3, 5, 3, 2] and print 3

"""


def firstDuplicate(a):
    my_set = set()
    for i in a:
        if i in my_set:
            return 1
        my_set.add(i)
    return - 1
