"""Pyramid with "+-+" Pattern
Construct a pattern like below with the given size.

    +
   +-+
  +---+
 +-----+
+-------+
"""

def pattern(num:int) -> str:
  rows =''
  k=1
  for j in range(1,num+1):
    space = (num-j)*' '
    row = '+'
    if j==1:
      i=1
    else:
      i=1
      while(i<=k):
        row += '-'
        i += 1
      k+=2
      row += '+'
    rows= rows+space+row+'\n'
  return rows

def format_plus_minus_pyramid(n: int) -> str:
    ## Write Code Here
    return pattern(n)

print(format_plus_minus_pyramid(10))
