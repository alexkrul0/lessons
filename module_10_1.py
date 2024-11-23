import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    i = 1
    while i <= word_count:
        file.write(f'Какое-то слово № {i}\n')
        time.sleep(0.1)
        i += 1
    print(f'Завершилась запись в файл {file_name}')
    file.close()

time1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time2 = datetime.now()
print(f'Работа функций {time2 - time1}')
print('')



time3 = datetime.now()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1.start()
thread1.join()
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2.start()
thread2.join()
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3.start()
thread3.join()
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread4.start()
thread4.join()
time4 = datetime.now()
print(f'Работа потоков {time4 - time3}')
