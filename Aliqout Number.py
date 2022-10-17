"""Aliqout Number The aliquot of a number is defined as the sum of the proper divisors of a number.

Example - 1: aliquot of 15 = 1 + 3 + 5 = 9

Example - 2: aliquot of 30 = 1 + 2 + 3 + 5 + 6 + 10 + 15 = 42

Note : aliquot of any prime is 1.

Write a function that determines the aliquot of a given number. """


def aliquot_number(n: int) -> int:
    # Write your code here
    sum = 0
    if(n<=0):
      return 1
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            sum+=i
    return sum   

aliquot_number(1)
