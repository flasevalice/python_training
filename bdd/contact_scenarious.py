from pytest_bdd import scenario
from .contact_steps import *


@scenario('contacts.feature', 'Add new contact')
def test_add_contact():
    pass


@scenario('contacts.feature', 'Delete a contact')
def test_delete_contact():
    pass


@scenario('contacts.feature', 'Modify some contact')
def test_modify_some_contact():
    pass