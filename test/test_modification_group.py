from model.group import Group


def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first_group(Group(name="update1", header="update2", footer="update3"))
    app.session.logout()


