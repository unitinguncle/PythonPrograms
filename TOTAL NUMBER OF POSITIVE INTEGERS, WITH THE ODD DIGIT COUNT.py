#TOTAL NUMBER OF POSITIVE INTEGERS, WITH THE ODD DIGIT COUNT Given an integer n, find the total number of positive integers, with the odd digit count, less than n. For example, if n is 786, the answer would be 9(1-digit numbers) + 687(3-digit numbers).

#Examples : total_positive_odd_digit_count(786) -> 696 total_positive_odd_digit_count(45) -> 9

#Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

def isodddigit(num:int) -> bool:
    digitno = 0
    while(num!=0):
        print(digitno)
        digitno += 1
        num //= 10
    print(digitno)
    if digitno%2!=0:
        return True
    return False
