"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""

class Stack:
    def __init__(self, N):
        self.elements = [0] * N
        self.size = 0

    def push(self, x):
        self.element[self.size] = x
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.element[self.size]
        else:
            return None
    
    def is_empty(self):
        return self.size == 0

# 100%
def solution(S):    
    N = len(S)
    stack = Stack(N)
    open_brackets = {'{', '[', '('}
    corresponding_closed_bracket = {'{':'}', '[':']', '(':')'}
    need_open_bracket = True   
    for bracket in S:        
        if bracket not in open_brackets:
            if need_open_bracket:
                return 0
            else:
                current_open_bracket = stack.pop()
                bracket_needed = corresponding_closed_bracket[current_open_bracket]
                if bracket != bracket_needed:
                    return 0
        else:
            stack.push(bracket)
            need_open_bracket = False
        if stack.is_empty():
            need_open_bracket = True
    if stack.is_empty():
        return 1
    else:
        return 0