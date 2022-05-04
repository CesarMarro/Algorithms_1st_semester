import random
#Generate 100 random numbers between 1 and 1000
def large_small(randomlist):

  a = randomlist[0]

  for i in range(len(randomlist)):
    if randomlist[i] < a:
      a = randomlist[i]
  print ("el valor minimo es: ",a)

  for i in range(len(randomlist)):
    if randomlist[i] > a:
      a = randomlist[i]
  print ("el valor maximo es: ",a)

  return " "
 