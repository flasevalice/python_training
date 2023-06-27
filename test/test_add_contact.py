# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("n1", "mn1", "ln1", "nik1", "D:\Lol\Снимок3.png", "t1", "comp1", "addr1",
                                       "1111111", "222222", "33333", "444444",
                                       "test@mail.ru", "test2@mail.ru", "test3@mail.ru", "http://test.ru",
                                       "1", "January", "1970", "2", "February", "1980",
                                       "addr2", "454545454", "note1")
    app.contact.fill_full_contact_info(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
