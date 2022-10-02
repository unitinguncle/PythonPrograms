"""Figures to Words (Western Style)
Write a function to convert figures to words in Western Number System using Dictionary:

1367 -> "One thousand three hundred and sixty seven"

18934345 -> "Eighteen million nine hundred and thirty four thousand three hundred and forty five"

Note: You can assume that the numbers are below 1 trillion"""

tens={2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninty"}
ones={0:"", 1:" one", 2:" two", 3:" three", 4:" four", 5:" five", 6:" six", 7:" seven", 8:" eight", 9:" nine"}
twenty={10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"forteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"ninteen"}
places=("", " thousand", " million", " billion", " trillion")

def digits3(num:str, ctr:int) -> str:
  word=""
  num = int(num)
  if (num//100) != 0:
    digit = ones[num//100]
    if(ctr == 1):
      word =word + digit + " hundred and "
    else:
      word =word + digit + " hundred "
  num %= 100
  if (num<10):
    word = word + ones[num%10]
  elif (num<20):
    word += twenty[num]
  else:
    word += tens[num//10] + ones[num%10]
  return word
   
  
 def figures2words(n: int) -> str:
    ## Write Code Here
    n = str(n)
    ctr =0
    inwords = ''
    while(n!=''):
      last3 = n[-3:]
      n=n[:-3]
      inwords = places[ctr] + inwords
      ctr += 1
      word = digits3(last3, ctr)
      inwords = word + inwords
    return (inwords.strip()).capitalize()

figures2words(18934345)
