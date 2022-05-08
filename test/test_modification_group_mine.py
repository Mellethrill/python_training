from model.group import Group


def test_modification_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modification_first_group(Group(name="update1", header="update2", footer="update3"))


