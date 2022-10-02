"""Collatz Sequence
Start with any number. (For practice try small numbers) say 7

If it is even divide by 2, if it is odd multiply by 3 and add 1

Repeat

This process reaches at ...4, 2, 1 and then starts repeating

Write a function that generates the sequence ending in 4, 2, 1 for the given starting number

For example  7  should generate [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]"""

def sequence():
  num = 7
  result = [7]
  while(True):
    if num%2==0:
      num/=2
      result.append(int(num))
    else:
      num*=3
      num+=1
      result.append(int(num))
    if result[-3:]==[4,2,1]:
      break
  print(result)
sequence()
