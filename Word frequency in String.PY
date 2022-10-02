"""Word frequency in String
Write a function to get frequency of each word in the sentence arranged in the descending order of the frequency.

Sample Input:

"Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected." """

def cleanText(string: str) -> list:
  word=''
  string += ''
  listedWords=[]
  for x in string:
    if x.isalpha() and x!=' ':
      word += x
    else:
      if word != '':
        listedWords.append(word)
        word=''
  
  return listedWords

from typing import Dict
import operator

def get_word_frequency(sent: str) -> Dict[str, int]:
    # Write Code Here
    words = cleanText(sent)
    dict1 = {}
    for x in words:
      wordCount = words.count(x)
      dict1.update({x:wordCount})
    sorted_d = dict(sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_d

get_word_frequency("Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.")
