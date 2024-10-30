

def custom_write(file_name, strings):
    name = file_name
    file = open(name, 'a', encoding='utf-8')
    string_positions = {}
    num = 1


    for i in strings:
        ft = file.tell()
        file.write(i + '\n')
        position = (num, ft)
        string_positions[position] = i
        num += 1
    file.close()
    return string_positions

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
