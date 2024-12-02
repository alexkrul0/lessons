from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

im = Image.open('cat.bmp')  # Получил изображение из файла
print(im.format, im.size, im.mode)  # Получил информацию об изображении: формат, размер и режим цветопередачи

#im.show()  # Просмотр исходного изображения

new_im = im.resize((1020,764))  # Изменение размеров изображения
trans_im = new_im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)  # Зеркальное преобразование, слева на право
trans_im.show()  # Просмотр измененного изображения

best_im = trans_im.filter(ImageFilter.DETAIL)  # Применение фильтровЖ
contr_im = ImageEnhance.Contrast(best_im)   # Изменение контраста
contr_im.enhance(1.3).show()
best_im.show()   # Просмотр улучшенного изображения
best_im.close()

with Image.open('cat.bmp') as res_im:  # Преобразование файла из формата .bmp в .jpg
    res_im.save('cat.jpg')




