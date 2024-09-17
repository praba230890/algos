"""
INPUT:
A = {5, 2, 4, 6, 1, 3}

CODE:
for j == 2 to A.length
    key = A[j]
    // insert A[j] into the sorted sequence A[1....j-1]
    i = j - 1
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i + 1
    A[i + 1] = key
"""

from collections.abc import Iterable


def insertion_sort(seq:Iterable):
    for j in range(1, len_a:=len(seq)):
        key = seq[j]
        i = j - 1
        while i > -1 and seq[i] > key:
            seq[i+1] = seq[i]
            i -= 1
        seq[i+1] = key
    return seq

seq = [5, 2, 4, 6, 1, 3]
print(insertion_sort(seq))