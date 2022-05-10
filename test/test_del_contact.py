from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", phone_home="1",
                            phone_mobile="1", phone_work="1", phone_fax="1", email1="test@ya.ru", email2="test@ya.com", email3="test@ya.net", homepage="test", address2="test", phone2="test", notes="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
