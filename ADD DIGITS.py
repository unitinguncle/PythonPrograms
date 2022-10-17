"""ADD DIGITS

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38 Output: 2 Explanation: The process is 38 --> 3 + 8 --> 11 11 --> 1 + 1 --> 2 Since 2 has only one digit, return it. Example 2:

Input: num = 0 Output: 0 """

def sum_of_digits(n:int)->int:
    sum=0
    while(n!=0):
        sum+=n%10
        n=n//10
    return sum


def add_digits(num: int) -> int:
    #write your code here
    while(num>9):
      if(num==0):
        return num
      num = sum_of_digits(num)
    return num

add_digits(38)
#sum_of_digits(38)
