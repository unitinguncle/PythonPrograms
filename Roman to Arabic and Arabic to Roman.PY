"""Roman to Arabic and Arabic to Roman
Implement two functions that converts roman number to arabic number and vice versa

Example:

roman2arabic("V") --> 5

arabic2roman(9) --> "IX" """

roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def nestedA2R(num:int) -> str:
  rstr=''
  if(num<10):
    rstr = roman[num]
    
def roman2arabic(roman_number: str) -> int:
    ## Write Code Here
    s = roman_number
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

def arabic2roman(arabic_number: int) -> str:
    ## Write Code Here
    roman_str=''
    while arabic_number > 0:
      for k,v in roman.items():     
        while arabic_number >= k:
          roman_str += v
          arabic_number -= k
    return roman_str
print(roman2arabic("V"))
print(arabic2roman(9))
