def add(*args):
    sum = 0
    for i in args:
        sum += i

    return sum

def multiply(*args):
    product = 1
    for i in args:
        product *= i

    return product

def prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        
    return result

def amstNumber(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        return True
    else:
        return False
    
def is_perfect_number(n):
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i: 
                divisor_sum += n // i
    divisor_sum -= n  
    return divisor_sum == n

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

    
