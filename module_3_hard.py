def calculate_sum_and_length(data):
    total_sum = 0
    total_length = 0

    if isinstance(data, (list, tuple, set)):
        for item in data:
            item_sum, item_length = calculate_sum_and_length(item)
            total_sum += item_sum
            total_length += item_length
    elif isinstance(data, dict):
        for key, value in data.items():
            key_sum, key_length = calculate_sum_and_length(key)
            value_sum, value_length = calculate_sum_and_length(value)
            total_sum += key_sum + value_sum
            total_length += key_length + value_length
    elif isinstance(data, str):
        total_length += len(data)
    elif isinstance(data, (int, float)):
        total_sum += data

    return total_sum, total_length

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_length = calculate_sum_and_length(data_structure)
print("Сумма всех чисел:", total_sum)
print("Общая длина всех строк:", total_length)