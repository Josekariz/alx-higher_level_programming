#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns the length of a string & its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
