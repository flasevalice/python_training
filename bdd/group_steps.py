from pytest_bdd import given, when, then
from model.group import Group


@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <logo> and <comment>', target_fixture="new_group")
def new_group(name, logo, comment):
    return Group(name=name, logo=logo, comment=comment)


@when('I add the group to the list', target_fixture="add_new_group")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new list is equal to the old list with the add group',
      target_fixture="verify_group_added")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
