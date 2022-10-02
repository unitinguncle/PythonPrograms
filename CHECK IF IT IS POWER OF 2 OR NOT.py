#CHECK IF IT IS POWER OF 2 OR NOT Write a function that takes an integer as input and returns True if the integer is a power of 2 otherwise the function should return False.

#Example - 1: Input : 4 Output : True

#Example - 2: Input : 45 Output : False

#Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

def is_power_of_two(num):
    #Write your code here
    x=1
    while x<=num:
        if x==num:
            return True
        x *= 2
    return False
