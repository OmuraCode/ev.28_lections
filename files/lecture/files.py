# работа с файлами

# каретка - указатель - курсор

# open(<путь до файла>)

# file = open("/Users/aibekworllld/Desktop/ev.28/lecture/files.py") # абсолютный путь
# file = open('files.py') # относиткельный путь (относительно той директории в которой вы работаете) 


# Режимы работы с файдами
# 1. Чтение -> r/r+ (read)
# 2. Записи -> w/w+ (write)
# 3. Добавление -> a/a+ (append)
# b, x, t

# file = open('text.txt', 'r')
# print(file.read())
# file.close()


# file = open('text.txt')
# data = file.read().split('\n')
# # data = data.split('\n')
# print(data)
# file.close()


# Контекстный менеджер 

# with open('text.txt') as file: # file = open('text.txt')
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')

# print(file, 'outside')



# file.tell() ->возвращает индекс где находится каретка(курсор)
# file.seek(index) - > перемещает курсор на индекс которй вы передалти

# with open('text.txt', 'r') as file:
#     print(file.readline().replace('\n', '')) 
#     print(file.tell())
#     file.seek(0)
#     print(file.readline().replace('\n', ''))
    # print(file.readlines()[2])
    # file.read()
    # print(file.tell())
    # print(file.readline())


# with open('text.txt', 'r') as file:
    # print(file.readline(8))
    # print(file.readlines(5))
    # print(file.read(5))



# with open('text.txt', 'w') as file:
#     file.write('Pervaya stroka\n')
#     file.write('John Snow is Bastard of Ned Stark\n')
#     file.write('This is lessons about files\n')
#     file.seek(0)
#     data = ['Bilal is genius\n', 'Tima is good boy\n']
#     file.writelines(data)




# with open('text.txt', '+a') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())


try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re

def get_imei_code(image):
    string = pytesseract.image_to_string(image)
    # print(string, type(string))
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)

    with open('imei_codes.txt', 'w') as file:
        file.writelines(f'{x}\n' for x in list_of_imei)


image = 'imei.jpg'
get_imei_code(image)



