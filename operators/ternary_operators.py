# sentence = input('Vvedite predlojenie: ')
# if sentence[-1] == '?':
#     print('Yes voprositelnoe!')
# else:
#     print('No, normal one!')
# ________________________________________


# Ternary operators - в одну строчку с одним условием
# sentence = input('Vvedite predlojenie: ')
# print('Yes voprositelnoe!' if sentence[-1]== '?' else 'No normal onne')


# Ternary operators (тернарный оператор) -  это конструкция которая по своему действию аналогична 
# конструкции if/else, но при этом записывается в одну строчку



number = int(input('Vvedite chislo: '))
res = 'even number' if number % 2 == 0 else 'odd number'
       # четное                              #нечетное 
print(res)



# Syntax ---->
# <выражение если True> if <условие> else <выражение если False>



# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)

#2
# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Inavalid choice')

#3
# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid chice!'
# print(res)


# ____________________________________

# CALCULATOR

# flag = True
# symbol = '0123456789' + '-' + '.' #0123456789-.

# while flag: 
#     print()

#     num1 = input('Введите первое число: ')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbol:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
    

#     num2 = input('Введите второе число; ')
#     is_correct_number = True
#     for x in num2:
#         if x not in symbol:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
    

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)

#     operator = input('Введите оператор(+, -, *, /): ').strip()


#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результат: {num1 / num2}') 
#     else:
#         print('Вы ввели неверный оператор!')

#     choice = input ('Хотите продолжить (yes/no)? ')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print('Пoka!')
    






    




































