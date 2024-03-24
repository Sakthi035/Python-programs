def gcdit(a, b):
    while b:
        a, b = b, a % b
    return a

print(int(gcdit(3,9)))