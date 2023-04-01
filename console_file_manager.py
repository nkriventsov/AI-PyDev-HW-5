# 2. В проекте реализовать следующий функционал:
# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
# - создать папку;
# - удалить (файл/папку);
# - копировать (файл/папку);
# - просмотр содержимого рабочей директории;
# - посмотреть только папки;
# - посмотреть только файлы;
# - просмотр информации об операционной системе;
# - создатель программы;
# - играть в викторину;
# - мой банковский счет;
# - смена рабочей директории (*необязательный пункт);
# - выход.
# Так же можно добавить любой дополнительный функционал по желанию.
#
# Описание пунктов:
# - создать папку
# после выбора пользователь вводит название папки, создаем её в рабочей директории;
# - удалить (файл/папку)
# после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
# - копировать (файл/папку)
# после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
# - просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;
# - посмотреть только папки
# вывод только папок которые находятся в рабочей папке;
# - посмотреть только файлы
# вывод только файлов которые находятся в рабочей папке;
# - просмотр информации об операционной системе
# вывести информацию об операционной системе (можно использовать пример из 1-го урока);
# - создатель программы
# вывод информации о создателе программы;
# - играть в викторину
# запуск игры викторина из предыдущего дз;
# - мой банковский счет
# запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
# - смена рабочей директории (*необязательный пункт)
# усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
# - выход
# выход из программы.
# Так же можно добавить любой другой интересный или полезный функционал по своему желанию
# После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход

# def console_file_manager_function():


'''
Лекция 7:
ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать)
и сохранить туда содержимое рабочей директории следующим образом: сначала все файлы, потом все папки,
пример как может выглядеть итоговый файл.
    files: victory.py, bill.py, main.py
    dirs: modules, packages
'''

'''
Лекция 8:
0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала;
1. Где это возможно переписать код с использованием генераторов и тернарных операторов;
2. Там где возможны исключительные ситуации добавить обработку исключений;
3. *Где это возможно применить декораторы.
Иногда может быть так, что применить новые возможности негде, особенно декораторы - это нормально.

ДОПОЛНИТЕЛЬНО:
Написать тесты для всех новых функций в проекте.
4. Создать pull request на объединение веток master и новой ветки, прислать ссылку на pull request как решение дз"
'''


import os
import shutil
import sys
import platform
import pathlib
import json


global current_dir
current_dir = os.getcwd()


def print_lines(f):
    def inner(*args, **kwargs):
        print('-' * 50)
        result = f(*args, **kwargs)
        print('-' * 50)
        return result
    return inner


if __name__ == '__main__':

    def main_menu():
        global main_menu_dict
        main_menu_dict = {
            1: ('Создать папку', create_dir),
            2: ('Удалить (файл/папку)', remove_file_dir),
            3: ('Копировать (файл/папку)', copy_dir),
            4: ('Просмотр содержимого рабочей директории', dir_review),
            5: ('Сохранить содержимое рабочей директории в файл', listdir_export),
            6: ('Посмотреть только папки', review_only_dir),
            7: ('Посмотреть только файлы', review_only_files),
            8: ('Просмотр информации об операционной системе', os_review),
            9: ('Создатель программы', file_owner),
            10: ('Играть в викторину', quiz),
            11: ('Мой банковский счет', p_account),
            12: ('Смена рабочей директории', change_working_directory),
            13: ('Выход', continue_or_exit),
        }

        def menu_choice():
            while True:
                try:
                    choice_result = int(input(f'\nВыберите пункт меню: '))
                    if choice_result > len(main_menu_dict) or choice_result < 1:
                        raise ValueError()
                except ValueError:
                    print('Некорректное значение!')
                    continue
                else:
                    return choice_result
                    break

        print(f'\nГлавное меню: \n')


        @print_lines
        def menu_print():
            for i in main_menu_dict:
                print('{:>3}{:^3}{:<45}'.format(i, ':', main_menu_dict[i][0]))
            return
        menu_print()

        choice = menu_choice()

        return choice


    def run_submenu_function():
        submenu_choice = main_menu()
        return main_menu_dict[submenu_choice][1]()

    # - выход
    # выход из программы.
    def continue_or_exit():
        continue_or_exit_choice = input('\nДля продолжения нажмите 1 для выхода 2: ')
        if continue_or_exit_choice == '2':
            sys.exit()
        return continue_or_exit_choice

    # - создать папку
    # после выбора пользователь вводит название папки, создаем её в рабочей директории;
    def create_dir():
        new_dir_name = input('Введите название папки: ')
        if not os.path.exists(new_dir_name):
            os.mkdir(new_dir_name)

    # - удалить (файл/папку)
    # после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
    def remove_file_dir():
        continue_delete_file_dir = None
        while continue_delete_file_dir != '2':
            delete_file_dir = input('Введите название фйла или папки на удаление: ')
            if os.path.isfile(delete_file_dir):
                os.remove(delete_file_dir)
                break
            elif len(os.listdir(delete_file_dir)) == 0:
                os.rmdir(delete_file_dir)
                break
            else:
                folder_tree_remove = None
                while folder_tree_remove != '1' or '2':
                    folder_tree_remove = input(
                        'Пакпка содержит файлы. Для подтверждения удаления нажмите 1 для отмены 2: ')
                    if folder_tree_remove == '1':
                        shutil.rmtree(delete_file_dir)
                        break
                    elif folder_tree_remove == '2':
                        continue_delete_file_dir = input(
                            'Для продолжения процесса удаления нажмите 1, для выхода в главное меню 2: ')
                        break
                    break

    # - копировать (файл/папку)
    # после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
    def copy_dir():
        copied_file_name = os.path.join(current_dir, input('Введите название копируемого файла/папки: '))
        new_file_name = os.path.join(current_dir, input('Введите название создаваемого файла/папки: '))

        shutil.copy(copied_file_name, new_file_name) if os.path.isfile(copied_file_name) else shutil.copytree(copied_file_name, new_file_name)

    # - просмотр содержимого рабочей директории
    # вывод всех объектов в рабочей папке;
    def dir_review():
        for item in os.listdir():
            print(item)

    def listdir_export():

        LISTDIR_FILE = 'listdir.txt'

        with open(LISTDIR_FILE, 'w') as lf:

            files = []
            dirs = []

            for item in os.scandir(current_dir):
                if item.is_file():
                    files.append(item.name)
                elif item.is_dir():
                    dirs.append(item.name)

            lf.write('Files: ' + ', '.join(files) + '\nDirs: ' + ', '.join(dirs))

    # - посмотреть только папки
    # вывод только папок которые находятся в рабочей папке;
    def review_only_dir():
        for item in os.scandir(current_dir):
            if item.is_dir():
                print(item.name)

    # - посмотреть только файлы
    # вывод только файлов которые находятся в рабочей папке;
    def review_only_files():
        for item in os.scandir(current_dir):
            if item.is_file():
                print(item.name)

    # - просмотр информации об операционной системе
    # вывести информацию об операционной системе (можно использовать пример из 1-го урока);
    def os_review():
        print(f'\n{sys.platform}')
        print(platform.platform())

    # - создатель программы
    # вывод информации о создателе программы;
    def file_owner():
        if __name__ == '__main__':
            print(f'\nID создателя программы: {os.stat(__file__, follow_symlinks=False).st_uid}.')

    # - играть в викторину
    # запуск игры викторина из предыдущего дз;
    def quiz():
        from HW_3_Quiz_Game.victory import quiz_game
        quiz_game()

    # - мой банковский счет
    # запуск программы для работы с банковским счетом из предыдущего дз (задание учебное,
    # после выхода из программы управлением счетом в главной программе сумму и историю покупок
    # можно не запоминать);
    def p_account():
        from HW_4_Personal_Account.use_functions import personal_account
        personal_account()

    # - смена рабочей директории (*необязательный пункт)
    # усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь.
    # Меняем рабочую директорию на ту что ввели и работаем уже в ней;
    def change_working_directory():
        global current_dir

        dir_path = pathlib.Path.home()
        print('\n{:<45}{:}'.format('Путь домашнего каталога:', dir_path))
        print('{:<45}{:}'.format('Путь текущего рабочего каталога:', current_dir))

        while True:
            try:
                new_working_dir = input('\nВведите путь к новой рабочей директории: ')
                if os.path.isabs(new_working_dir) is True:
                    if os.path.exists(os.path.abspath(new_working_dir)) is False:
                        raise OSError()
                elif os.path.exists(os.path.join(dir_path, new_working_dir)) is False:
                    raise OSError()
            except OSError:
                print('Некорректный путь!')
                continue
            else:
                if os.path.isabs(new_working_dir) is True:
                    current_dir = os.chdir(os.path.join(new_working_dir))
                    print('{:<45}{:}'.format('Путь выбранного текущего рабочего каталога:', os.getcwd()))
                else:
                    current_dir = os.chdir(os.path.join(dir_path, new_working_dir))
                    print('{:<45}{:}'.format('Путь выбранного текущего рабочего каталога:', os.getcwd()))
            break
        return current_dir


    run_submenu_function()

    while True:
        try:
            continue_or_exit_choice = continue_or_exit()
            if continue_or_exit_choice == '1':
                run_submenu_function()
                continue
            elif continue_or_exit_choice != '1' and continue_or_exit_choice != '2':
                raise ValueError()
            else:
                break
        except ValueError:
            print('Некорректное значение!')
            continue


    # console_file_manager_function()





