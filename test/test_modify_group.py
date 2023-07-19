from model.group import Group
import random


def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New first group"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    group.name = Group(name="New group").name
    # group_id = old_groups[int(group.id)].id
    app.group.modify_group_by_id(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups[group.id] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
