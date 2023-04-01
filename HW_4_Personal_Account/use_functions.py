"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


'''
Лекция 7:
ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл. 
 
При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета 
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл
 
При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
'''


def personal_account():
    import os
    import sys
    import json

    BALANCE_FILE_NAME = os.path.join(sys.path[0], 'balance.csv')
    PURCHASE_HISTORY_FILE_NAME = os.path.join(sys.path[0], 'purchase_history.json')

    balance = 0
    purchase_history = {}

    if os.path.exists(BALANCE_FILE_NAME):
        with open(BALANCE_FILE_NAME, 'r') as f:
            try:
                balance = int(f.read())
            except ValueError:
                pass

    if os.path.exists(PURCHASE_HISTORY_FILE_NAME):
        with open(PURCHASE_HISTORY_FILE_NAME, 'r') as jf:
            try:
                purchase_history = json.load(jf)
            except ValueError:
                pass

    def print_lines():
        print('-' * 30)

    def continuation():
        result = input('Для продолжения нажмите "Ввод"!')
        while result != '':
            result = input('Для продолжения нажмите "Ввод"!')


    while True:
        print(f'\nТекущий баланс: {balance}\n')
        print_lines()
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        print_lines()
        choice = input(f'\nВыберите пункт меню: ')
        if choice == '1':
            add_balance = int(input('Введите сумму пополнения: '))
            if add_balance <= 0:
                print('Пополнение возможно только положительной суммой!')
                continuation()
            else:
                balance += add_balance
        elif choice == '2':
            new_purchase_price = int(input(f'\nВведите сумму покупки положительным значением: '))
            if new_purchase_price <= 0:
                print('Введение суммы покупки возможно только положительной суммой!')
                continuation()
            else:
                if new_purchase_price > balance:
                    print(f'Недостаточно средств - на счету {balance}!')
                    continuation()
                else:
                    purchased_item_name = input('Введите наименование покупки: ')
                    purchase_history.update({purchased_item_name: new_purchase_price})
                    balance -= new_purchase_price
        elif choice == '3':
            print_lines()
            print("{:<20} {:<10}".format('Наименование', 'Стоимость'))
            print_lines()
            for k, v in purchase_history.items():
                print('{:<20} {:<10}'.format(k, v))
            print_lines()
            continuation()
        elif choice == '4':
            with open(BALANCE_FILE_NAME, 'w') as f:
                f.write(str(balance))
            with open(PURCHASE_HISTORY_FILE_NAME, 'w') as jf:
                json.dump(purchase_history, jf)
            break
        else:
            print('Неверный пункт меню')

# personal_account()