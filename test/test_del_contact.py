from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    app.contact.delete_first_contact()
