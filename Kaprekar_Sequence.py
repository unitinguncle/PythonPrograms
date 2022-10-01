#Kaprekar's Sequence
#Take any four-digit number, using at least two different digits (leading zeros are allowed).

#Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.

#Subtract the smaller number from the bigger number.

#Go back to step 2 and repeat.

#This process stops after a few steps, that is step 3 produces the same number.

#  9541 – 1459 = 8082

#  8820 – 0288 = 8532 

#  8532 – 2358 = 6174  

#  7641 – 1467 = 6174 
#Given a suitable starting number generate the sequence, stopping the output without any repetition.

#Input:  1945 

#Output:  [1945,8082,8532,6174]

#---------------------------------------
def sequence(num:int) -> int:
  myList=[]
  for x in str(num):
    myList.append(int(x))
  
  string=''
  myList.sort(reverse = True)

  for x in myList:
    string=string+str(x)
  largeno = int(string)

  string=''
  myList.sort()

  for x in myList:
    string=string+str(x)
  smallno = int(string)

  return (largeno - smallno)

from typing import List

def kaprekar_seq(n: int) -> List[int]:
    myList=[n]
    difference=sequence(n)
    
    while(True):
      myList.append(difference)
      difference=sequence(myList[-1])
      if(difference == myList[-1]):
        break

    return myList
kaprekar_seq(1945)
