calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    t_ = (len(string), string.upper(), string.lower())
    count_calls()
    return t_


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    for i in list_to_search:
        i = i.upper()
    is_cont = True
    if string in list_to_search:
        is_cont = False
    return is_cont


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
