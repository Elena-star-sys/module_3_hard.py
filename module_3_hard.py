data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    sum_numbers = 0
    sum_string = 0
    def recurse(data):
        nonlocal sum_numbers, sum_string
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                recurse(item)
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        elif isinstance(data, int) or isinstance(data, str):
            if isinstance(data,int):
                sum_numbers += data
            if isinstance(data, str):
                sum_string += len(data)
    recurse(data_structure)

    return sum_numbers + sum_string


result = calculate_structure_sum(data_structure)
print(result)







