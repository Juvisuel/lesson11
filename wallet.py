# import random

def decor_all(f):
    def inner(*args, **qwargs):
        print('*' * 100)
        result = f(*args, **qwargs)
        print('*' * 100)
        return result
    return inner


@decor_all
def refill(money_old, counter_old):
    money_add = int(input('введите сумму пополнения: '))
    money_new = money_old + money_add
    counter_old += 1
    print('баланс = ', money_new)
    return money_new, counter_old, money_add


@decor_all
def buy(money_old, counter_old):
    cost_item = int(input('введите цену покупки: '))
    if cost_item <= money_old:

        money_new = money_old - cost_item
        counter_old += 1
        cost_name = input('средств достаточно. Введите наименование покупки: ')
        print('баланс = ', money_new)
    else:
        print('на вашем счете недостаточно средств')
        cost_name = 0
        money_new = money_old
        pass

    return [cost_name, cost_item, money_new, counter_old]


@decor_all
def buy_stories(buy_dict):
    for item, value in buy_dict.items():
        print(f'Номер операции: {value[1]} Покупка: {item}, стоимость: {value[0]}')


def cassa(transactions):
    for item, value in transactions.items():
        print(f'Номер операции: {item} Расход/приход: {value[0]}, ,баланс: {value[1]}')


def wallet(money, counter, buy_dict, transactions):

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. история операций')
        print('5. выход')

        choice = input('Выберите пункт меню ')

        if choice == '1':
            money_new, counter, money_add = refill(money, counter)
            transactions[counter] = [money_add, money_new]
            money = money_new
            print(money, counter)

        elif choice == '2':
            cost_name, cost_item, money_new, counter = buy(money, counter)
            buy_dict[cost_name] = [cost_item, counter]
            transactions[counter] = [-1 * cost_item, money_new]
            money = money_new

        elif choice == '3':
            buy_stories(buy_dict)

        elif choice == '4':
            cassa(transactions)

        elif choice == '5':
            print('до встречи')
            # print(transactions)
            # print(buyDict)
            break
        else:
            print('Неверный пункт меню')

    print(f'баланс = {money}, номер последней операции {counter}')

    return money, counter, buy_dict, transactions
