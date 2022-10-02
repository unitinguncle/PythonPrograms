#mon(th) dd yyyy -> yyyyddd
#We are given data strings of the form

#"mon(th) dd, yyyy"

#Examples:

#Jan 4,2012

#February 07 1987

#may 30, 1999
#The month name may or may not be capitalised
#The month name may be spelt out in full or just the first three letters
#(Minimum three is guaranteed)
#The day may or may not have a leading zero
#The day and year will be separated by either
#Comma or
#Space or
#Comma and a space
#The task is convert such strings to the seven digit number yyyyddd, where ddd is the dddth day of the year

#Jan 4, 2012 ⇒2012004

#February 07 1987 ⇒1987038

#may 30, 1999 ⇒1999150

#Solution:
#1st function -
#leap year - function takes 4 digit int as input, return True/False

#2nd function -
#clean up, split, validation - list/dict of months,days different collection(tuple) for 30/31

#return (leap?, mon, date, year)

#if date is invalid (0, "", 0, 0)

#3rd function -
#dictionary contains cummulative days - jan:0, feb:31, march:59, apr: 90


def isleapyear(year:int) ->bool:
  if year%400==0 and year%100==0:
    return True
  elif year%4==0 and year%100!=0:
    return True
  else:
    return False
    
MONTH_31 = ("JAN","MAR","MAY","JUL","AUG","OCT","DEC")
MONTH_30 = ("APR","JUN","SEP","NOV")

def dateFormatting(date:str) -> tuple:
  list1 = date.replace(',',' ').split()
  year = int(list1[2])
  leap = isleapyear(year)
  month = list1[0].upper()[:3]
  date = int(list1[1])

  if(month not in MONTH_31 and month not in MONTH_30 and month != "FEB"):
    return (0,"",0,0)

  if date < 1 or date > 31:
    return (0,"",0,0)
  
  if month == "FEB":
    if date > 28 + leap:
      return (0,"",0,0)

  if month in MONTH_30 and date > 30:
    return (0,"",0,0)
  
  return (leap, month, date, year)
  
def dateShortner(date:str) -> str:
  is_leap, month, date, year = dateFormatting(date)
  if month=="":
    return "ERROR"
  days = {"JAN":0, "FEB":31, "MAR": 59, "APR":90, "MAY":120, "JUN":151, "JUL":181, "AUG":212, "SEP":243, "OCT":273, "NOV":304, "DEC":334}
  output = year
  day = days[month]
  output *=1000
  if is_leap and (month!='JAN' or month!='FEB'):
    output = output +day +date
  else:
    output = output +day +date +1
  print(output)

dateShortner("jun 15, 2012")
