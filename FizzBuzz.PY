"""FizzBuzz (Using Dict)
Write a function that accepts the limit and prints the numbers from 1 to limit

Rules:

For the multiples of 3 print "FIZZ" instead of the number
For the multiples of 5 print 'BUZZ'.
For the multiples of both 3 and 5 print "FIZZBUZZ"
Else print the number """

def fizzbuzz(num:int) -> str:
  (divby3, divby5) = (num%3==0, num%5==0)
  fizzbuzzdict = {
      (True, True):'fizzbuzz',
      (True, False): 'fizz',
      (False, True): 'buzz',
      (False, False): str(num)
  }
  
  return (fizzbuzzdict[(divby3, divby5)])
  
valueList = []
for i in range(1,51):
  valueList.append(fizzbuzz(i))
valueList
