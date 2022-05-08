import math

def check_prime(number):
    sqrt_number = math.sqrt(number)
    print(f"sqrt:{sqrt_number}")
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
    return True

print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
print(f"check_prime(10,000,019) = {check_prime(10_000_019)}")
print(f"check_prime(4) = {check_prime(4)}")
