# -*- coding: utf-8 -*-
from group4 import Group
from application4 import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="asdasf", header="agafasf", footer="agafasf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="", header="", footer=""))
    app.logout()
