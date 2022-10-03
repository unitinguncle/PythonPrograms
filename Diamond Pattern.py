
"""Diamond Pattern
Construct a pattern like below with the given size.

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
    """

def star(le:int, num:int) -> str:
  space = (num-le)*' '
  st = ' *'*le
  return space+st

def diamond(num:int) -> str:
  diamondP = ''
  for i in range(1,num+1):
    diamondP += star(i,num) + '\n'
  for i in range(num-1,0,-1):
    diamondP += star(i,num) + '\n'
  return diamondP

def format_diamond_pattern(n: int) -> str:
    ## Write Code Here
    return diamond(n)

print(format_diamond_pattern(5))
