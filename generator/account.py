# -*- coding: utf-8 -*-
import os

import jsonpickle as jsonpickle

from model.account import Account
import random
import string

f = "data/account.json"


def random_string(max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "Autotest" + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_email(max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))]) + "@autotest.com"


test_data = [
    Account(
        username=random_string(7),
        email=random_email(8),
        emplyeeuri="",
        isenable=True
    )
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
