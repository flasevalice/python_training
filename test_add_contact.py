# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_full_contact_info(Contact("n1", "mn1", "ln1", "nik1", "D:\Lol\Снимок3.png", "t1", "comp1", "addr1",
                                       "1111111", "222222", "33333", "444444",
                                       "test@mail.ru", "test2@mail.ru", "test3@mail.ru", "http://test.ru",
                                       "1", "January", "1970", "2", "February", "1980",
                                       "addr2", "454545454", "note1"))
    app.logout()

