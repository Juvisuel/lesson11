import born_fay_forever
import wallet
import os_work

money = wallet.money_check()
counter = 0
buyDict = wallet.buy_dict_check()
transactions = {}

while True:
    print('1. работа с папками и файлами')
    print('2. работа с финансами')
    print('3. игра')
    print('4. автор')
    print('5. завершить работу')

    choice_up = int(input('Выберите пункт меню '))

    if choice_up == 1:

        os_work.os_work()

    elif choice_up == 2:

        money1, counter1, buyDict1, transactions1 = wallet.wallet (counter, transactions)
        money, counter, buyDict, transactions = money1, counter1, buyDict1, transactions1

    elif choice_up == 3:
        born_fay_forever.born_fay_forever()

    elif choice_up == 4:
        print('* *'*10)
        print('творец сущего непознаваем и бесконечен')
        print('* *' * 10)

    elif choice_up == 5:
        print('* *' * 10)
        print('до встречи!')
        break

    else:
        print('пожалуйста, отнеситесь к выбору внимательнее')
