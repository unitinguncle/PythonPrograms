"""Check if a Sentence is Palindrome?
Implement a function to check if a sentence is a palindrome or not.

Note: ignore white spaces and other characters to consider sentences as palindrome.

Example:

is_palindrome("A man, a plan, a canal: Panama") ➞ True"""

def removeSpace(text:str) -> str:
  newString=""
  for ch in text:
    if ch.isalpha():
      newString += ch
  return newString

def is_palindrome(text: str) -> bool:
  text = removeSpace(text)
  return text==text[::-1]
