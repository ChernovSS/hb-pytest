# -*- coding: utf-8 -*-
import data

from fixture.account import AccountHelper
from fixture.application import Application
from model.account import Account

account = Account(username='test1111',email='test1@test.com')

app = Application()
app.open_home_page()
app.login()

ah = AccountHelper(app=app, wd=app.wd)
ah.open_accounts_url()
# ah.get_account_list(account)

new_account = Account(username="autotest", email="test1@test.com")
ah.create(new_account)

# app.destroy()

