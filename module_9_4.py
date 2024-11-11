from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        name = file_name
        file = open(name, 'w', encoding='utf-8')
        for data in data_set:
            file.write(str(data))
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word = choice(self.words)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Ну а вдруг', 'Скорее всего')
print(first_ball())
print(first_ball())
print(first_ball())
