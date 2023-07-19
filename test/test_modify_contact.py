import random

from model.contact import Contact
from random import randrange


def test_modify_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    old_contacts = db.get_contact_list()
    # index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    contact = Contact(firstname="New firstname").firstname
    contact.id = old_contacts[contact.id].id
    app.contact.modify_contact_by_id(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts[contact.id] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
