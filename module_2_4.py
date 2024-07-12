numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
len_list = len(numbers)
for i in range(1, len_list):
    is_prime = True
    n = numbers[i]
    for j in range(2, n - 1):
        if n % j == 0:
            is_prime = False
            # print(f'{n}  % {j} = {n % j} - {is_prime}')
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
print(primes)
print(not_primes)