from model.group import Group


def test_modification_group(app):
    app.group.modification_first_group(Group(name="update1", header="update2", footer="update3"))


