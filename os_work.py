import os
import shutil


def os_work():
    while True:

        print('1. создать папку')
        print('2. удалить файл/папку')
        print('3. копировать файл/папку')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть папки')
        print('6. посмотреть файлы')
        print('7. посмотреть инфо о системе')
        print('8. смена директории')
        print('9. вернуться в главное меню')

        choice = input('Выберите пункт меню ')

        work_path = os.getcwd()
        # print('рабочий путь',work_path)

        if choice == '1':
            name_new = work_path + '/' + input('какую папку будем создавать? ')
            os.mkdir(name_new) if not os.path.exists(name_new) else print('такая папка уже существует')

        if choice == '2':
            print(os.listdir(work_path))
            name_new = work_path + '/' + input('что будем удалять? ')
            os.rmdir(name_new) if os.path.exists(name_new) else print('такой папки не существует')

        if choice == '3':
            print(os.listdir(work_path))
            name_old = input('что копируем? имя + расширение')

            name_new = input('как назовем? имя + расширение')
            path_and_file_old = work_path + '/' + name_old
            path_and_file_new = work_path + '/' + name_new

            try:
                shutil.copyfile(path_and_file_old, path_and_file_new)

            except FileNotFoundError:
                print('такого файла/папки не существует')

        if choice == '4':
            print(os.listdir(work_path))  # посмотреть содержимое директории

        if choice == '5':
            for dirname in os.listdir(work_path):
                temp_path = work_path + '/' + dirname
                if os.path.isdir(temp_path):
                    print("Каталог:", os.path.join(temp_path))

        if choice == '6':
            # посмотреть файлы
            for filename in os.listdir(work_path):
                if os.path.isfile(work_path + '/' + filename):
                    print("Каталог:", os.path.join(work_path + '/' + filename))

        if choice == '7':
            print('окружение', os.environ)

        if choice == '8':
            print('текущая директория', work_path)
            os.chdir(input('введите новый путь'))
            print(os.getcwd())

        if choice == '9':
            break
