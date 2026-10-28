def max_num(*numbers):
    if len(numbers)==0:
        return None
    largest=numbers[0]
    for n in numbers:
        if n> largest:
            largest=n
            
    return largest
print(max_num(3, 12, 32, 9, 21))