def amstNumber(number):
    originalnum = number
    if number == 0:
        return 0
    else:
        num = str(number)
        length = len(num)
        sum = 0
        for i in range(0, length):
            sum = sum + pow(number % 10, length)
            number = number // 10
        
    if sum == originalnum:
        return True
    else:
        return False
    
a = int(input("Enter a number:"))
b = amstNumber(a)
if b == True:
    print("amstrong number.")
else:
    print("not an amstrong number.")
