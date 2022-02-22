def transform_string(number: int) -> str:
    if number == 1 or (number > 20 and number % 10 == 1):
        return f'{number} процент'
    elif (1 < number < 5) or (number > 20 and 1 < number % 10 < 5):
        return f'{number} процента'
    else:
        return f'{number} процентов'


for n in range(1, 101):
    print(transform_string(n))
