

def is_prime(func):
    def wrapper(*args):
        count = 0
        sum_ = sum(args)
        for i in range(2, sum_ // 2):
            if sum_ % i == 0:
                count +=1
        if count <= 0:
            print('Простое')
        else:
            print('Составное')

        return func(*args)

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)