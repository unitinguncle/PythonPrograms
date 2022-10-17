
"""HARSHAD NUMBER

A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples: is_harshad(75) ➞ False

7 + 5 = 12 75 is not exactly divisible by 12

is_harshad(171) ➞ True

1 + 7 + 1 = 9 9 exactly divides 171 """

def is_harshad(num: int)-> bool:
    #write your code here
    num2 = num
    sum =0
    while(num2!=0):
        sum += num2%10
        num2=num2//10
    if num%sum==0:
        return True
    else:
        return False

is_harshad(171)
