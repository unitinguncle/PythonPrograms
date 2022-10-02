"""ROT 13
Implement a function which accepts a string as an argument and generates the ROT13 Caesar Cipher.

The ROT-13 (i.e. rotate by 13 places) method is a very simple encryption method, in which one replaces each letter of the alphabet with the 13th letter after it. So, ‘A’ becomes ‘N’, ‘B’ becomes ‘O’ and so on. This method is a special case of the Caesar Cipher, with which Caesar encoded his letters in the ancient Rome.

Here is our approach for encoding a given string:

Check if given input has all valid characters, i.e every character is an alphabet [a - z or A - Z] - function is_string() returns "True" if the char is an alphabet.

As the next step we need to add 13 to character and encode the character- rot13() returns the encoded character of the input character

Now we generate the encoded string using the function - generate_encrypted_string() which returns encoded string """

def is_string(character: str) -> bool:
  return character.isalpha()

def rot13(text: str) -> str:
    ## Write code Here
    letters = "abcdefghijklmnopqrstuvwxyz"
    capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newString=''
    ch=text
    if is_string(ch):
       if ch.isupper():
         index = capitalLetters.index(ch)
         index +=13
         if(index>=26):
           index-=26
         newString += capitalLetters[index]
       else:
         index = letters.index(ch)
         index +=13
         if(index>=26):
           index-=26
         newString += letters[index]
    else:
       newString += ch
    return newString
  
def generate_encrypted_string(text:str) -> str:
  newString = ''
  for ch in text:
    newString += rot13(ch)
  return newString

generate_encrypted_string("NPCI Talentsprint")
