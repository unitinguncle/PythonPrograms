#IS THE WORD AN ISOGRAM An isogram is a word that has no duplicate letters.

#Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

#Examples :

#is_isogram("Algorism") ➞ True is_isogram("PasSword") ➞ False # Not case sensitive. is_isogram("Consecutive") ➞ False

#Note : Please return your output. Don't print your answer inside the function. Your code will not get evaluated, if you are using 'print statement' inside the function.

def is_isogram(s: str)-> bool:
    #Write your code here
    s=s.lower()
    for x in s:
        if s.count(x)>1:
          print(s)
          return False
    return True
is_isogram("PasSword")
