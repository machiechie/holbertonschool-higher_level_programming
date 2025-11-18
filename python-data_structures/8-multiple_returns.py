#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_word = None
    else:
        first_word = sentence[0]
        return(len(sentence), first_word)
