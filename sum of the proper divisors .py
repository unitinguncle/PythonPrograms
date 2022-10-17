"""Classify the Number If the sum of the proper divisors of a number is equal to the number itself, it is called a perfect number. Examples: 6 and 28

If the sum of the proper divisors of the number is greater than the number itself, we call the number an abundant number. Example: 12

If the sum of the proper divisors of the number is less than the number itself, we call the number a deficient number. Example: all primes, all powers of 2

Write a function that classifies a number as above. It should return 0 if the argument is perfect, -1 if deficient and +1 if abundant

Example 1: classify(6) -> 0

Example 2: classify(12) -> 1

Example 3: classify(13) -> -1"""

def sum_of_divisor(n:int) -> int:
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum

def classify(k: int) -> int:
    #Write your code here
    if(sum_of_divisor(k)==k):
        return 0
    elif(sum_of_divisor(k)<k):
        return -1
    elif(sum_of_divisor(k)>k):
        return 1
    
