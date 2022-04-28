import json
import os
import shutil

def save_workdir_to_file(work_path):
    work_names = os.listdir(work_path)
    list_dir = []
    list_files = []
    for file_dir in work_names:
        if os.path.isfile(work_path+'/'+file_dir):
            list_files.append(file_dir)
        else:
            list_dir.append(file_dir)
    all_dict =  {}
    all_dict['files'] = list_files
    all_dict['dirs'] = list_dir

    with open(' listdir.txt', 'w') as temp_file:
        json.dump(all_dict, temp_file)


def os_work(choice = 7):

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
            name_new = work_path+'/'+input('какую папку будем создавать? ')
            if not os.path.exists(name_new):
                os.mkdir(name_new)
            else:
                print('такая папка уже существует')

        if choice == '2':
            print(os.listdir(work_path))
            name_new = work_path + '/' + input('что будем удалять? ')
            if os.path.exists(name_new):
                os.rmdir(name_new)
            else:
                print('такой папки не существует')


        if choice == '3':
            print(os.listdir(work_path))
            name_old = input('что копируем? имя + расширение')

            if os.path.exists(name_old):
                name_new = input('как назовем? имя + расширение')
                shutil.copyfile(work_path+'/'+name_old, work_path+'/'+name_new)
            else:
                print('такого файла/папки не существует')

        if choice == '4':
            print(os.listdir(work_path))   # посмотреть содержимое директории
            save_workdir_to_file(work_path)

        if choice == '5':
            for dirname in os.listdir(work_path):
                if os.path.isdir(work_path+'/'+dirname):
                    print("Каталог:", os.path.join(work_path+'/'+dirname))


        if choice == '6':
            # посмотреть фйлы
            for filename in os.listdir(work_path):
                if os.path.isfile(work_path+'/'+filename):
                    print("Каталог:", os.path.join(work_path+'/'+filename))

        if choice == '7':
            print('окружение', os.environ)

        if choice == '8':
            print('текущая директория', work_path)
            os.chdir(input('введите новый путь' ))
            print(os.getcwd() )

        if choice == '9':
            break


