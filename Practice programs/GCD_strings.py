def gcd_of_strings(str1, str2):
    
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    if str1[:len(str2)] != str2:
        return ""
    
    while len(str2) > 0:
        if str1 == str2 * (len(str1) // len(str2)):
            #print((len(str1) // len(str2)))
            return str2
        str2 = str2[:-1]
    
    return ""

str1 = "abcabc"
str2 = "abc"
largest_divisor = gcd_of_strings(str1, str2)
print(largest_divisor)