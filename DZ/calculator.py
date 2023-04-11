# num1 = float (input('Введите первое число: '))
# num2 = float (input('Введите второе число: '))
# operation = input('Выберите операцию из следующих: - , + , / , // , % , * , **: ')

# if operation == '-':
#     print('Ответ:', num1 - num2)

# elif operation == '+':
#     print('Ответ: ', num1 + num2)

# elif operation == '*':
#     print('Ответ: ', num1 * num2)

# elif operation == '/':
#     if num2 == 0:
#         print('Делить на ноль нельзя!')
#     elif num2 != 0:
#         print('Ответ: ', num1 / num2)

# elif operation == '//':
#     if num2 == 0:
#         print('Делить на ноль нельзя!')
#     elif num2 != 0:
#         print('Ответ: ', num1 // num2)

# elif operation == '%':
#     if num2 == 0:
#         print('Делить на ноль нельзя!')
#     elif num2 != 0:
#         print('Ответ: ', num1 % num2)

# elif operation == '**':
#     print('Ответ: ', pow(num1, num2))

# else:
#     print('Данной операции нет в системе!')





# ______________________________________

# Таблица умножения
for i in range(1, 10):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}\n')
    