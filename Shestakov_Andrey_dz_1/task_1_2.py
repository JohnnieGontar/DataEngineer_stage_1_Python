def generate_cube_list(start: int, end: int) -> list:
    my_list = []
    for idx in range(start, end + 1):
        cube = f'{idx ** 3}'
        sum_num = 0
        for num in cube:
            sum_num += int(num)

        if sum_num % 7 == 0:
            my_list.append(idx)

    return my_list


def sum_list_1(dataset: list) -> int:
    all_sum = 0
    for num in dataset:
        all_sum += num
    return all_sum


def sum_list_2(dataset: list) -> int:
    all_sum = 0
    cur_num_sum = 0
    for num in dataset:
        for cur_num in str(num + 17):
            cur_num_sum += int(cur_num)
        if cur_num_sum % 7 == 0:
            all_sum += num
    return all_sum


my_list = generate_cube_list(1, 1000)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
