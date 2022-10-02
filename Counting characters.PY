"""Counting characters
Implement a function to count vowels, consonants, digits and special characters in a given string

Input:

count_characters("learn.npci.2022@talentsprint.com")

Output:

(7, 17, 4, 4)
"""

string = "learn.npci.2022@talentsprint.com"

def fun(string):
  dig,vow,cons,spc=0,0,0,0
  for ch in string:
    if ch.isdigit():
      dig+=1
    elif ch.isalpha():
      if ch in 'aeiouAEIOU':
        vow+=1
      else:
        cons+=1
    else:
      spc+=1
  out=(vow,cons,dig,spc)
  print(out)
  
fun(string)
