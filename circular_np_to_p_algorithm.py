import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def circular_np_to_p(n):
    if n % 4 != 0 or n < 8:
        return None

    for p in range(3, n // 2 + 1, 2):
        q = n - p
        if p != q and is_prime(p) and is_prime(q):
            return (p, q)
    return None

# Example usage
for n in range(8, 100, 4):
    result = circular_np_to_p(n)
    if result:
        print(f"{n} = {result[0]} + {result[1]}")
    else:
        print(f"No valid primes found for {n}")
