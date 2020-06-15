# открыть картинку и преобразовать ее в numpy массив
from PIL import Image
import numpy
im = Image.open(r'C:/python/gazprom.png')
im  = im.convert('L') # делает картинку черно-белым
pixels = numpy.asarray(im) # массив данного изображения

im_1 = Image.fromarray(pixels, 'L') #преобразовать из массива в изображение
im_1.save ("Watch_r.jpg") #создать файл изображения
