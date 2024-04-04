# i=0
# while i < 3:
#     print(i)
#     i=i+1
# print(i+1)


# l=list("1234")
# l[0]=l[1]=5
# print(l)

#return a pattern
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15
# count=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()



# a = [1, 2, 3, 4, 5, 6]

# for a[-1] in a:
#     print(a[-1])

#return a first palindrome word in a given list
# strs = ["sat", "mom", "dad", "lucky"]

# for i in strs:
#     st = list(i)
#     revers = st[::-1]
#     if revers == st:
#         print("".join(st))
#         break
#     else:
#         continue

#pattern printing
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5 or (i == 3 and j == 3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print() 


# s = ['h','e','l','l','o']
# for i in s:
#     s = s[::-1]

# print(s)

# reverse a string using two pointer aprouch
# s = ['H', 'a', 'n', 'n', 'a', 'h']
# class Solution:
#     def reverseString(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = s[ : :-1]



# Solution().reverseString(s)
# print(s)

# x =123
# x = int(str(x)[::-1])


# print(x)

# s = "loveleetcode"

# for i in range(0,len(s)):
#     if(s[i] not in s[i+1:len(s)]):
#         print(i)
#         break

# def firstUniqChar(s: str) -> int:
#     char_count = {}
    
#     # Count occurrences of each character
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     # Find the first character with count 1
#     for i, char in enumerate(s):
#         if char_count[char] == 1:
#             return i
    
#     # If no unique character found, return -1
#     return -1

# # Example usage:
# s = "leetcode"
# print(firstUniqChar(s))  # Output: 0 (the first 'l' is the first non-repeating character)


# s = "cat"
# t = "tar"
# charcounts ={}
# for char in s:
#     if char in charcounts:
#         charcounts[char] += 1
#     else:
#         charcounts[char] = 1
    
# for i, char in enumerate(t):
#     if char in charcounts:
#         charcounts[char] -= 1
#     else:
#         print("false")
# else:
#     if all(count == 0 for count in charcounts.values()):
#         print("true")
#     else:
#         print("false")
# charcounts.ge

# s =" "
# pal = []
# for i in s.lower():
#     if i.isalpha():
#         pal.append(i)
#     else:
#         pass

# reverse = pal[::-1]
# if pal == reverse:
#     print("t")
# else:
#     print("f")
# print(reverse)
# print(pal)

# s = "words and 987"
# a = []
# for i in s:
#     if i == ' ':
#         continue
#     elif i == "-" or i == "+":
#         a.append(i)
#     elif i.isdigit():
#         a.append(i)
    
# b = int(''.join(str(i) for i in a))


# if b >= 2**31 or b <= 2**31-1:
#     print(b)

#strs = ["flower","flow","flight"]

# word1 = "flower"
# word2 = "flow"
# result = ""
# i = 0
# while i < len(word1) and i < len(word2):
#     result += word1[i] + word2[i]
#     i +=1

# result += word1[i:]

# result += word2[i:]

# print(result)

# s = "ABABAB"
# t = "ABAB"

# minstr = min(s , t)
# maxstr = max(s , t)
# #print(minstr)

# if minstr in maxstr:
#     print(minstr)


# def gcd_of_strings(str1, str2):
#     # Ensure str1 is not shorter than str2
#     if len(str1) < len(str2):
#         str1, str2 = str2, str1
    
#     # Check if str2 divides str1
#     if str1[:len(str2)] != str2:
#         return ""
    
#     # Find the largest common divisor
#     while len(str2) > 0:
#         if str1 == str2 * (len(str1) // len(str2)):
#             print((len(str1) // len(str2)))
#             return str2
#         str2 = str2[:-1]
    
#     return ""
# \

# # Example usage
# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# largest_divisor = gcd_of_strings(str1, str2)
# print(largest_divisor)  # Output: "ABC"

# def gcdit(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(int(gcdit(3,9)))

# def gcdre(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcdre(b, a % b)
    
# print(gcdre(90,18))

# def mincoin(coins , amount):
#     coins.sort(reverse = True)
#     mincoin = 0
#     coinr =[]

#     for coin in coins:
#         while coin <= amount:
#             amount -= coin
#             mincoin += 1
#             coinr.append(coin)
#     #coinr.append(coins[len(coins)-1])
#     return mincoin, coinr

# coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
# amount = 1246
# print(mincoin(coins, amount))
# y =0
# z =88
# x = y and z
# print(x)



# a = 2
# b = 5
# x = 10 
# xy = lambda a , b: a * b
# print(xy(x,a))


