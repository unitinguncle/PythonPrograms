"""Pascal's Triangle
          1
        1    1
     1    2    1
   4    3    3   1
1    4    6    4    1
The triangle can be constructed by first placing a 1 along the left and right edges.
Then the triangle can be filled out from the top by adding together the two numbers just above to the left and right of each position in the triangle.
Thus, the third row, in Hindu-Arabic numerals, is 1 2 1, the fourth row is 1 4 6 4 1, the fifth row is 1 5 10 10 5 1, and so forth.
The first row, or just 1, gives the coefficient for the expansion of  (x+y)0=1 ; the second row, or  1 1 , gives the coefficients for  (x+y)1=x+y ; the third row, or 1 2 1, gives the coefficients for  (x+y)2=x2+2xy+y2 ; and so forth.
Note:

It is possible to use the formula for  nCr  and calculate each element and then format them. But a simpler method is to consider the following:

Let us think of each row as a list: first row is  [1] , second is  [1,1] ; third is  [1,2,1] 
so how do we go from  [1]−>[1,1]−>[1,2,1] """

from math import factorial
def make_pascal(size: int) -> str:
    ## Write Code Here
    for i in range(size):
      for j in range(size - i + 1):
        print(end = "  ")

      for j in range(i + 1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end = "   ")
      print()

make_pascal(6)
