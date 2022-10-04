"""Clean Data (using functional paradigm)
Cleaning data is a vital element in any data analysis. This involves removing unwanted characters from the data at hand.

Write a Python function clean_data(data) that reads the content of the string passed as input. The function should remove all the non-alphanumeric characters except space from the contents, (only keep letter, number and space) and return the cleaned data in a list.

If the input data has multiple lines seperated by '\n', the output lists should contain strings which are individual 'cleaned lines'.

The output list should not contains any empty string (if a line does not have non-alphanumeric).

Sample Input 1:

data: the data content as string
Sample Output 1:

a list of strings
Examples:

clean_data('where are you?\nwh@t is going on?')should return ['where are you', 'wht is going on']

clean_data("[^_^))]\nYou're invited, though you shouldn't drink?") should return ['Youre invited though you shouldnt drink'] """

def is_acceptable(ch:str) -> bool:
  return (ch == ' ' or ch.isalpha() or ch.isdigit())

def string_list(line:str) -> str:
  list1 = list(filter(is_acceptable, line))
  return ''.join(list1)

from typing import List

def clean_data(data: str) -> List[str]:
    ## Write Code Here
    list2 = data.split('\n')
    result = list(filter(string_list,list2))
    return result

clean_data("[^_^))]\nYou're invited, though you shouldn't drink?")
