def geomentricSequence(firstTerm, ratio, NthTerm):

    # print(firstTerm*pow(ratio,i))1
    if NthTerm == 1:
        print(firstTerm)
        return firstTerm
    else:
        # i =i+11
        a = geomentricSequence(firstTerm, ratio, NthTerm - 1) * ratio
        print(a)
        return a
    
a = int(input("Enter the First Term of the sequence:"))
r = int(input("Enter the ratio of the Geomentric Sequence"))
n = int(input("Enter the Nth Term of the sequence:"))
print("The geomentric sequence is: ")

print("The value of N th Element is",geomentricSequence(a, r, n))