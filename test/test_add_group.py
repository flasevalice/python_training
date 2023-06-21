# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="one", logo="logo1", comment="comment1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", logo="", comment=""))
