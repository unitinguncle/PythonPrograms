#MINIMUM VALUE TO BE ADDED Given a list of integers, which may be negative or positive, find the minimum number which when added to every element will make the whole list positive, i.e., every element will become strictly greater than zero.

#For example, if the list is [-4, -3, 89, -6, -25] the answer would be 26. If we add 26 to each element present in the list, then list becomes [22, 23, 115, 20, 1]. Now all the elements in the list are greater than zero. So the answer is 26.

#Examples :

#min_val([-4, -3, 89, -6, -25]) -> 26 min_val([32, 12, -45, -44, -33]) -> 46

#Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

def min_val(lst: [int])-> int:
    #Write your code here
    min=lst[0]
    for a in lst:
        if a<min:
            min = a
    if min>=0:
      return min
    return (min*-1)+1
