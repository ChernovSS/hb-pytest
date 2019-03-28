# -*- coding: utf-8 -*-

from model.account import Account


def test_add_account(app, accounts):
    account = accounts
    old_list = app.Account.get_account_list(account)
    app.Account.create(account)
    new_list = app.Account.get_account_list(account)
    old_list.append(account)
    assert sorted(old_list, key=Account.username) == sorted(new_list, key=Account.username)
