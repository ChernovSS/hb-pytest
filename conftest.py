# -*- coding: utf-8 -*-

import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application

fixture = None
target = None




@pytest.fixture
def app():
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])



def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
