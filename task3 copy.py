#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
  
(3 points)
"""
sortMe = {1: -2, 2: 6, 4: 0, 6: 1, 9: 2, 10: 3, 11: 0, 13: 3, 14: 4, 15: -2, 17: 0, 18: -1, 20: 3}

def sortkeys():
  global sortMe
  temp = []
  for i in sortMe:
    temp.append(i)
  temp.sort()
  tempReturn = []
  for i in temp:
    tempReturn.append(sortMe[i])
  return tempReturn
print(sortkeys())

def sortValue():
  global sortMe
  temp = []
  for i in sortMe:
    temp.append(sortMe[i])
  temp.sort()
  tempreturn = []
  for i in temp:
    tempreturn.append(get_key(temp[i]))
  return tempreturn

def get_key(val):
   
    for key, value in sortMe.items():
        if val == value:
            return key


print(sortValue())