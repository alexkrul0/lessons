import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r')
    line = file.readline()
    while line:
        all_data.append(line)
        line = file.readline()
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# time1 = datetime.now()
# for filename in filenames:
#     read_info(filename)
# time2 = datetime.now()
# print(time2 - time1, '(линейный подход)')



if __name__ == '__main__':
    time3 = datetime.now()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(read_info, filenames)

    pool.close()
    pool.join()

    time4 = datetime.now()
    print(time4 - time3, '(многопроцессный подход)')