#CHECK IF PART OF THE INTEGER 
#Write a function that takes an integer(n) and a list of digits(lst) as inputs and returns True if we can create "n" by concatenating a few elements from lst and returns False otherwise. All the elements of "lst" are between 0 and 9.

#Examples : is_part_of_integer([6, 3, 4], 634) ➞ True Explanation: (if we concatenate the given lst then we'll get 634, which is equivalent to given n value. So it returns True.) is_part_of_integer([5, 2, 6, 3, 4], 263)) ➞ True Explanation: (if we concatenate the given lst then we'll get 52634, where n = 263 which is a part of num. So it returns True.) is_part_of_integer([2, 5, 3, 4], 5890) ➞ False

#Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

#Answer:(penalty regime: 0 %)

def is_part_of_integer(lst: [int], n: int)-> bool:
    #Write your code from here
    for x in str(n):
        if (int(x) not in lst):
            return False
    return True
