"""Common Elements (using functional paradigm)
Finding out common elements in various data structures is an important element in Data Analysis. Sometimes it tells us about patterns, other times customer interests, etc.

Write a Python function common_elements(data) that accepts a list of lists of number as input, and returns a list of elements which occurred in at least two lists in the in input. This list of common elements must be sorted, and contain no duplicates.

Sample Input:

data: a list of lists containing numbers
Sample Output:

a list of numbers, sorted in ascending order
Example:

common_elements([[10,20,30],[20,10,50],[60,40,80,50],[40],[40]]) should return [10, 20, 40, 50]

common_elements([[10],[20],[60,40,80,50],[70],[90]]) should return [] """

from functools import reduce
from typing import List

def common_elements(data: List[List[int]]):
    ## Write Code Here
    common = set()
    for i in range(len(data)):
      list1 = data[i]
      for j in range(len(list1)):
        no = list1[j]
        occ=1
        for k in range(len(data)):
          if no in data[k]:
            occ += 1
        if occ > 2:
          common.add(no)
    listed_output = list(common)   
    listed_output.sort() 
    return (listed_output)

common_elements([[10,20,30],[20,10,50],[60,40,80,50],[40],[40]])
