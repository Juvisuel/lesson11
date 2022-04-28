import wallet
import os_work
import os


def test_money_check():
    assert wallet.money_check() >= 0

def test_buy_dict():
    assert type(wallet.buy_dict_check()) == dict

def test_save_workdir_to_file():
    work_path = os.getcwd()
    assert  os_work.save_workdir_to_file(work_path) == None