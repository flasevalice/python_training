import random

from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, db):
    # если нет контактов, создаем контакт
    if len(db.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    # если нет группы, создаем группу
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New first group"))
    # список контактов
    contacts_db = db.get_contact_list()
    # список групп
    groups_db = db.get_group_list()
    # выбираем случайную группу
    rand_gr = random.choice(db.get_group_list())
    # выбираем случайный контакт из тех, у кого нет группы
    rand_cont = random.choice(db.get_contacts_not_in_group(Group(id='%s' % rand_gr.id)))
    # contacts_not_in_gr =
    # добавляем контакт в группу
    app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
    # добавить ассерты
    # print(contacts_not_in_gr)
    # contacts_in_group = orm.get_contacts_in_group(rand_gr.id))
    # print(contacts_in_group)
