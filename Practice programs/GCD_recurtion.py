def gcdre(a, b):
    if b == 0:
        return a
    else:
        return gcdre(b, a % b)
    
print(gcdre(90,18))