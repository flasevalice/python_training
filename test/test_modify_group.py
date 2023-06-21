from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="New group"))
