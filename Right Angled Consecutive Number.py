""" Right Angled Consecutive Number
Given a number  n  generate the following pattern

 1

 2  3

 4  5  6

 7  8  9 10

11 12 13 14 15

... n

**
where  n  is the last number. Note that this means

the last line has just two stars
the penultimate line may not be longer than the previous line.
Note:

This problem can result in a subtle bug. To test if your program has the bug, check your program with  n=10  and  n=9 

More importantly did you think in terms of printing a pyramid with some number of lines?

Is that the best abstraction?

Ask yourself:

how many numbers in say line 4?

how many numbers upto line 4?

is there a pattern to the last number in each line? """

def make_consecutive_number_triangle(n: int) -> str:
    ## Write Code Here
    i=1
    j=1
    while j<=n:
      for k in range(i):
        if j>n:
          break
        print(j,end=' ')
        j +=1
      i += 1
      print('\n')
    return '**'
print(make_consecutive_number_triangle(7))
