"""
Write a function that takes a sentence, strips white space and capitalisation, 
and checks if string is the same backwards
"""

# a[:,:,-1] --> reverse a

def solution(sentence):        
    stripped_sentence = sentence.replace(" ", "")   # strip all whitespace
    
    # OTHER STRIPPING POSSIBILITIES
    # sentence.strip                                # remove leading + trailing whitespace
    # " ".join(sentence.split())                    # remove all spaces, except singular spaces between words
    
    stripped_sentence = stripped_sentence.lower()        
           
    return stripped_sentence == stripped_sentence[::-1]