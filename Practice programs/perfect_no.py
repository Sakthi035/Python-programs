import math

def is_perfect_number(n):
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the square root twice for perfect squares
                divisor_sum += n // i
    divisor_sum -= n  # Exclude the number itself from the sum of divisors
    return divisor_sum == n

# Example usage:
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
