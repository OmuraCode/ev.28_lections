# postgreSQL - система управления БД(СУБД/DBMS)
# Это ряд программ и инструментов позволяюших соэдавать БД, управлять ею и манипулировать данными 
# внутри(CRUD)

# Postgres - сама база данных, она объектно-реляционная, то есть данные хранятся в виде таблиц и 
# таблицы имеют связи мужду собой

# SQL(Structured Query Language) - декларированный язык структурированных запросов, он применяктся 
# для создания и получения данных при помощи БД 



# ----------------
# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа
# exit

# команда для входа в своего юзера
# psql

# команда для выхода
# \q

# команда для Суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# команда для Суперюзера
# ALTER USER 'username' WITH PASSWORD '1'

# create DATABASE 'name'; #создание бд

# \l - список всех бд

# \du - все юхеры

# \dt - все таблицы (нужно подключиться к бд заранее)

# \d 'name' - подробная информация про таблицу(нужно подкл к бд заранее)

# \c 'name' - # команда для подключения к бд
# 
# psql -U <username> -d <dbname> -подключаемся под выбранным username к dbname 





# Kоманда для создания таблицы ->\
# CREATE TABLE <table name>(
#     <column> <type>
# )
# ->
# films_db=# CREATE TABLE films (
#     code char(5),
#     title varchar(100),
#     date date,
#     genre varchar(50),
#     budget integer,
#     country varchar(50),
#     id serial
#     );

# DROP TABLE <name> - удаление всей таблицы


# Kоманда для добавление данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);
# ->
# films_db=# INSERT INTO films (code, title, date, genre, budget, country) VALUES
# ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', 1000000, 'USA'), 
# ('het-5', 'Lord of Rings', '2001-06-12', 'Fantasy', 1200000, 'USA');


# Kоманда для получения данных
# SELECT (columns) * FROM <table>;


# Kоманда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;


# Kоманда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>

# ORDER BY: Он позволяет нам сортировать выводящие данные по убыванию или по возрастанию. ASC(по возрастанию) и DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tabelname> ORDER BY <row> = [ASC/DESC];

# WHERE: Используется для фильтраций по полям будут выводится только те данные которые соответсвуют условию оператору WHERE 
# Синтаксис: SELECT <row> FROM <tabelname> WHERE <row> = "Чему либо";


# BERWEEN: условие между
# Синтакси: SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответсвует введеному шаблону для сторк. Чуствителен к ригистру 
# ILEKE: Тоже самое но не зависит от ригистра
# Синтаксис: SELECT <row> FROM <tabelname> WHERE <row> = LIKE/ILIKE 'чему либо';

# AND: Оператор и, для множественых условий 
# IN: WHERE <row> in (1, 2, 3, 4, 5);

# LIMIT: Ставит ограниечение в кол-во получаемых данных

# GROUP BY: разделяет данные которые сы получаем в SEELECT, при этом группируя их по определенному признаку.
# И теперь для каждой группы можно использовать функцию

# HABING: ставит условие при помоши которго данные отбираются в группировке

# Агрегатные функции: AVG(), COUNT(), MIN(), MAX(), SUM()

# Экспорт БД(дамп): 
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>


# -----------------------------------------------------

# Типы полей в Postgres

# Numeric Types(числовые данные)

    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer (2 bytes) -> -2_147_... to 2_147_...
    # c. bigint(8 bytes) -> -8 to 8 infinite
    # d. real (4 bytes) -> число с плавающей точкой (6 цифр после запятой)
    # f. double precsion -> real но только с двойной точностью (12 цифр после запятой)
    # g. serial (4 bytes) -> integer, auto-increment


# Character types(символьные типы(строковые)):
#     a. varchar(кол-во символов) -> если мы укажем 50 символов, а заполним тольео 10, то остальные 
# будут свободны(Макс - 55)
    # b. char(кол-во символов) -> если мы укажем 50 символов, а заполним тольео 10, то остальные 
# будут заполнены пробелом (Макс - 55)
    # c. text() - неогр кол-во символов

# Boolean Type
    # a. boolean(1 bytes) -> True/False

# date - > календарная дата (гг.мм.дд)

# location -> координатная точка(x,y) = (243, 54)

#enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad')


# ------------------------------
# Связи между таблицами(relations)
    # 1. One to one - человек и паспорт
        # в одну из таблиц добавляется поле fk и дается ограничение unique

    # 2. One to Many - человек и банковские карты
        # в таблицу много(банковские карты) добавляется поле fk

    # 2. Many to Many - студенты и преподды
        # создается вспомогательная 3я таблица со связями

# Ограничения

    # 1 NOT NULL - обязательно к заполнению
    # 2. UNIQUE - то что будут хранится только уникальные данные
    # 3. CHECK -> CHECK age > 0 - ограничение проверки на условие
    # 4. PRIMARY KEY - для установки идентификатора данных в таблице
    # 5. FOREIGN KEY - (для установки связей между таблицами)
    # 6. ON DELETE - для установки поведения при удалении данных которые были связаны



# ----------------------------------
# JOIN - выборка данных из 2 таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы
# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, WHERE p1.id = o1 product_id; 
# Запрос сразу в две таблицы


# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1 product_id; 





def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        False

is_palindrome('erm')


