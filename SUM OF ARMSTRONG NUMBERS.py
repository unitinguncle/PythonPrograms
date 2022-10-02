#SUM OF ARMSTRONG NUMBERS Write a function that takes two integers, a and b as input and returns the sum of Armstrong numbers between two given integers.

#Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. (1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4 = 1 + 1296 + 81 + 256 = 1634, so 1634 is an armstrong number.)

#Examples : sum_of_armstrong(1, 500) -> 1346 (Armstrong numbers between 1 and 500 - 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407) sum_of_armstrong(200, 400) -> 741 (Armstrong numbers between 200 and 400 - 370, 371) Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

def is_armstrong(num:int) -> bool:
    count = 0
    num2 =num
    num3 = num2
    arm = 0
    while(num!=0):
        count+=1
        num//=10
    while(num2!=0):
        r=num2%10
        arm += pow(r,count)
        num2//=10
    if arm==num3:
        return True
    return False
  
def sum_of_armstrong(a, b):
    sum = 0
    for x in range(a,b):
        if is_armstrong(x):
            sum += x
    return sum
