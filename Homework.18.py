data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(structure):
    sum_ = 0
    if isinstance(structure, int):
        sum_ = sum_ + structure
    if isinstance(structure, str):
        sum_ = sum_ + len(structure)
    if isinstance(structure, list):
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, tuple):
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, set):
        structure = list(structure)
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, dict):
        structure = list(structure.items())
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    return sum_


result = calculate_structure_sum(data_structure)
print(result)
