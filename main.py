numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            break
    return True
for i in numbers:
    if i == 1:  # пропускаем число 1
        continue
    if is_prime(i):
        primes.append(i)
    else:
        not_primes.append(i)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)