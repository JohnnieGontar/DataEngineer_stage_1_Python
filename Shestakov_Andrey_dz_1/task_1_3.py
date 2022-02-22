def transform_string(number: int) -> str:
    if number == 100:
        return f'{number} процентов'
    elif number < 21:
        if 1 <= number <= 4:
            return f'{number} {check_ending(number)}'
        else:
            return f'{number} процентов'
    else:
        ls = []
        for n in str(number):
            ls.append(int(n))

        return f'{ls[0]}{ls[1]} {check_ending(ls[1])}'


def check_ending(number: int) -> str:
    if number == 1:
        return 'процент'
    elif 2 <= number <= 4:
        return 'процента'
    else:
        return 'процентов'


for n in range(1, 101):
    print(transform_string(n))
