my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
len_list = len(my_list)
while True:
    if i < len_list:
        n = my_list[i]
        if n == 0:
            i = i + 1
            continue
        elif n > 0:
            print(n)
            i = i + 1
            continue
        else:
            print("Следующее число отрицательное")
            break
    else:
        print("Конец списка")
        break