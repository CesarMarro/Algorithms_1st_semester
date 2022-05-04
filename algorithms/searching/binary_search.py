def binario(list,n):
    primero = 0
    ultimo = len(list)-1
    mitad = 0

    while primero <= ultimo :
        mitad = int((primero + ultimo)/ 2)
     
        if n == list[mitad]:
            return mitad

        elif n < list[mitad]:
            ultimo = mitad - 1
          
        else:
            primero = mitad + 1   
    return -1