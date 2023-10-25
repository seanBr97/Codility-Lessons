"""
    # Distinct values in an array A
"""

from collections import Counter

# O(N*log(N)) or O(N)
def solution(A):
    counts = Counter(A)
    return len(counts.keys())
    
    # Alternative
    # return len(set(A))