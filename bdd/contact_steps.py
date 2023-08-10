from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random


@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse('a contact with {firstname}, {lastname} and {middlename}'), target_fixture='new_contact')
def new_contact(firstname, lastname, middlename):
    return Contact(firstname=firstname, lastname=lastname, middlename=middlename)


@when('I add the contact to the list', target_fixture='add_new_contact')
def add_new_contact(app, new_contact):
    app.contact.fill_full_contact_info(new_contact)


@then('the new contact list is equal to the old list with the added contact',
      target_fixture='verify_contact_added')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fn_new"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list', target_fixture='delete_contact')
def delete_contact(app, random_contact):
    app.contact.delete_some_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact',
      target_fixture='verify_contact_deleted')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.contact_list(), key=Contact.id_or_max)


@when(parsers.parse('I modify the contact from the list to {firstname}, {lastname} and {middlename}'),
      target_fixture='modify_contact')
def modify_contact(app, random_contact):
    contact = random_contact
    contact.firstname = Contact(firstname="New firstname").firstname
    contact.lastname = Contact(lastname="New lastname").lastname
    contact.middlename = Contact(middlename="New middlename").middlename
    app.contact.modify_contact_by_id(contact)


@then('the new contact list is equal to the old list and contact is modified',
      target_fixture='verify_contact_list')
def verify_contact_list(db, non_empty_contact_list):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
