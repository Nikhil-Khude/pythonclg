def get_max(*num):
    if len(num) == 0:
        return None

    max_num = num[0]

    for n in num:
        if len(n) > len(max_num):
            max_num = n

    return max_num

print(get_max('arush', 'payal', 'zarina', 'yogesh'))
