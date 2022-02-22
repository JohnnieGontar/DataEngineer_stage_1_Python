def generate_cube_list(start: int, end: int) -> list:
    my_list = []
    for n in range(start, end + 1, 2):
        my_list.append(n ** 3)
    return my_list


def check_by_7(n: int) -> int:
    sum_n = 0
    for i in str(n):
        sum_n += int(i)
    if sum_n % 7 == 0:
        return n
    else:
        return 0


def sum_list_1(dataset: list) -> int:
    all_sum = 0
    for num in dataset:
        all_sum += check_by_7(num)
    return all_sum


def sum_list_2(dataset: list) -> int:
    all_sum = 0
    for num in dataset:
        all_sum += check_by_7(num + 17)
    return all_sum


my_list = generate_cube_list(1, 1000)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
