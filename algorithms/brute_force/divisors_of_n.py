
def divisor(n):

    x = n
    d = []
    
    for i in range (1, n+1):
        if n % i == 0 :
            d.append(i)

    return d

n = 893
result = divisor(n)
print ("numero: " + str(n) + " divisores: " + str(result))