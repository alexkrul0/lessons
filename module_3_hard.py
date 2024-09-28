def summator(*args):
    sum = 0
    for i in list(*args):
        if isinstance(i, list):
            sum += summator(i)
        elif isinstance(i, dict):
            sum += summator(list(i.items()))
        elif isinstance(i, set):
            sum += summator(list(i))
        elif isinstance(i, tuple):
            sum += summator(list(i))
        else:
            if isinstance(i, int):
                sum += i
            else:
                sum += len(i)

    return sum


data_structure = [
    [1, 2, 3], {'a':4, 'b':5},
    (6, {'cube':7, 'drum':8}), 'Hello',
    ((),[{(2, 'Urban', ('Urban2', 35))}])
]

print(summator(data_structure))