"""Find Intersection
Write a function, find_intersection(), that reads a list of two strings:

The first is a list of comma-separated numbers sorted in ascending order
The second element is another list of comma-separated numbers (also sorted)
Your goal is to return a string of numbers that occur in both elements of the input list in sorted order. If there is no intersection, return the string "No Intersection"

Sample Input 1:

["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

Sample Output 1:

"1, 4, 13"

Sample Input 2:

["11, 32, 43, 72, 138", "12, 26, 24, 113, 150"]

Sample Output 2:

"No Intersection" """

from typing import List

def find_intersection(arr: List[str]) -> str:
    ## Write Code Here
    l1=arr[0].split(',')
    l2=arr[1].split(',')
    output=[]
    for items in l1:
      if items in l2:
        output.append(items)
    combined = ','.join(output)
    return combined

find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])
