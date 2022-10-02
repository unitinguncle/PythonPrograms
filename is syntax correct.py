#Is Syntax Correct?
#Write a function that detects syntax errors in a string that contains nothing but parantheses.

#Sample input 1:  ((()) 

#Sample output 1: False

#Sample input 2:  ((((())))) 

#Sample output 2: True

#Sample input 3:  ))(( 

#Sample output 3: False

#-------------------------------------
def is_syntactically_correct(only_paran: str) -> bool:
    ## Write Code Here
    opening=0
    closing=0
    for ch in only_paran:
      if opening>=closing:
        if ch=='(':
          opening+=1
        elif ch==')':
          closing+=1
      else:
        return False
    if opening==0:
      return False
    if(opening==closing):
      return True
    else:
      return False

is_syntactically_correct("((())")
