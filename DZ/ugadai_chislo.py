from random import randint

name = input('Введите свое имя: ')
num = randint(1, 5)
guesses = 0

a = input(f'{name}, хотите сыграть в игру ? ')

if a.lower().strip() == 'нет':
    print("Сыграем в следующий раз!")
elif a.lower().strip() == "да":
    i = 0
    while i < 5:
        guess_num = int(input('Введите число от 1 до 5: '))
        guesses += 1
        if guess_num == num:
            otv = input(f"Поздравляем, вы угадали  с {guesses} попытки! Хотите ли вы сыграть еще раз? ")
            if otv.lower().strip() == "да":
                continue
            elif otv.lower().strip() == 'нет':
                print('Приходите к нам еще!')
                break
else:
    print("Выберите да/нет")   
            
    