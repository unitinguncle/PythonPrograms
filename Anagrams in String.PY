"""Anagrams in String
Write a function to get anagrams in the list of words in dictionary where key is sorted characters of each unique word and value is a list of anagram words.

Note: If any key in the dictionary has single element remove them.

Sample Input:

get_anagrams(['cat', 'dog', 'secure', 'true', 'god', 'tac', 'rescue', 'act', 'false'])
Sample Output:

{'act': ['cat', 'tac', 'act'], 'dgo': ['dog', 'god'], 'cersu': ['secure', 'rescue'], 'ertu': ['true'], 'aefls': ['false']} """

from typing import Dict, List

def get_anagrams(words: List[str]) -> Dict[str, List[str]]:
    ## Write Code Here
    dict1 = {}
    for x in range(0,len(words)):
      anaList=[]
      for y in range(len(words)):
        if sorted(words[x]) == sorted(words[y]):
          anaList.append(words[y])  
           
      dict1["".join(sorted(words[x]))]=anaList
     
    print(dict1)
get_anagrams(['cat', 'dog', 'secure', 'true', 'god', 'tac', 'rescue', 'act', 'false'])
