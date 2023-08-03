#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple of the first character and the
       string length
    """
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
