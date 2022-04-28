import random

from decor import decor_all

def born_fay_forever():
    hardcore = int(input('выберите сложность игры, 1 - сложно, 2 - средне, 3 - легко: '))

    celebrites = ['Мел Гибсон','Алексей Николаевич Толстой','Вольфанг Амадей Моцарт',
                  ' Галилео Галилей','Николай Коперник','Элизабет Тэйлор', 'Юрий Гагарин',
                  ' Элтон Джон', 'Джекки Чан', 'Николай Склифосковский']
    dates = ['3.01.1956', '10.01.1883','27.01.1756',
             '15.02.1564','19.01.1473','27.02.1932','9.03.1934',
             '25.03.1947','7.04.1954','6.04.1836']
    celeb_dates  = {}
    for i in range(len(celebrites)):
        celeb_dates[celebrites[i]] = dates[i]

    scores = 0
    game_scores = 0

    for i in range(6-hardcore):
        print(f'раунд {i+1}')
        random_choice = random.choice(range(9))
        celeb_game = list(celeb_dates.items())[random_choice]

        true_date = celeb_game[1]
        true_year = int(true_date[-4:])

        dust_dates = [true_date]
        for j in range(4-hardcore):
            dust_day = random.choice(range(1,28))
            dust_month = random.choice(range(1,12))
            dust_year = random.choice(range(true_year-25,true_year+25))
            dust_date = str(dust_day)+'.'+str(dust_month)+'.'+str(dust_year)
            dust_dates.append(dust_date)

        random.shuffle(dust_dates)

        print('назовите год рождения {}? '.format(celeb_game[0]))
        print('варианты ответа: ')
        for j, date in enumerate(dust_dates):
            print(f'{j+1}: {date}',end = '   ')

        @decor_all
        def ansver_score(ansver, scores, game_scores):
            # ansver = int(input('введите номер выбранного ответа '))
            if dust_dates[ansver - 1] == true_date:
                print('отлично!')
                scores += 1
            else:
                print(f'неверный ответ, правильный ответ {true_date}')
                game_scores += 1

            return scores, game_scores


        scores, game_scores = ansver_score(int(input('введите номер выбранного ответа ')), scores, game_scores )
        #
        # ansver = int(input('введите номер выбранного ответа '))
        # if dust_dates[ansver-1] == true_date:
        #     print('отлично!')
        #     scores += 1
        # else:
        #     print(f'неверный ответ, правильный ответ {true_date}')
        #     game_scores +=1


        #
        print('счет: игрок = {} - игра = {}'.format(scores,game_scores))
        print()

    print('итоговый счет: игрок = {} - игра = {}'.format(scores, game_scores))