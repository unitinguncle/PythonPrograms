"""THIRD LARGEST ELEMENT Given a list of positive integers return the third largest element. If the list is [5, 6, 8, 4, 3, 2] the answer would be 5.

Examples : third_largest([5, 6, 8, 4, 3, 2]) ➞ 5 third_largest([3, 7, 8, 9, 2]) ➞ 7 """


def third_largest(lst):
    #Write your code here
    for i in range(2):
        fst = max(lst)
        lst.remove(fst)
    return max(lst)
