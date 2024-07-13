first_range = range(3, 21)
second_range = range(1, 21)
print(first_range, second_range)
for i in range(len(first_range)):
    codes = []
    n = first_range[i]
    for j in second_range:
        if j == n:
            break
        for k in second_range:
            p = j + k
            if k < 2:
                continue
            if k == j:
                continue
            if n < p:
                break
            if j > k:
                continue
            if n % p == 0:
                codes.append([j, k])
                k += 1
                continue
    print(f'{n} - {codes}')