def combinacion(list1, list2):
  list1 = [1,4,9]
  list2 = [2,3,8]
  newlist = []

  i = 0
  j= 0 

  while i < len(list1) and j <len(list2):
    
    if list1[i] < list2[j]:
      newlist.append(list1[i])
      i += 1 
    else:
      newlist.append(list2[j])
      j += 1

  if i == len(list1):
    for k in range(j, len(list2)):
      newlist.append(list2[k])

  else:
    for k in range(i, len(list1)):
      newlist.append(list1[k])

  return newlist