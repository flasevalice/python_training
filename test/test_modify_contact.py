from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
