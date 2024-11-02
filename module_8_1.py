def add_everything_up(a, b):
    try:

        print(a + b)

    except TypeError:
        if isinstance(a, str):
            print(a + str(b))
        elif isinstance(b, str):
            print(str(a) + b)



add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
