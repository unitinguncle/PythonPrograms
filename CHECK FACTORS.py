#CHECK FACTORS Write a function that returns 1 if all integers in a list are factors of given integer n, and 0 otherwise.

#Examples :

#check_factors([2, 3, 4], 12) ➞ 1

#Since 2, 3, and 4 are all factors of 12.
#check_factors([1, 2, 3, 8], 12) ➞ 0

#8 is not a factor of 12.
#check_factors([1, 2, 50], 100) ➞ 1 check_factors([3, 6], 9) ➞ 0 Answer:(penalty regime: 0 %)

def check_factors(lst, n):
    #Write your code here
    for x in lst:
        if n%x != 0:
            return 0
    return 1
