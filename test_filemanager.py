import shutil
import os
import wallet


money_old = 100
counter_old = 1
money_add = 200
buy_dict = {1: ['сено', 100]}
transactions = {}
cost_item = 50

a = 5
b = 4
f = a + b



def test_wallet_buy_stories():
    assert wallet.buy_stories(buy_dict) == None

def test_cassa():
    assert wallet.cassa(transactions) == None

def test_refill():
    assert wallet.refill(money_old, counter_old, money_add) == (300, 2, 200)

def test_buy():

    assert wallet.buy(money_old, counter_old, cost_item) == [money_old-cost_item, counter_old+1]

