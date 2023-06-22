from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New first group"))
    app.group.modify_first_group(Group(name="New group"))
