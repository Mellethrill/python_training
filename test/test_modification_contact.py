from model.contact import Contact


def test_modification_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", phone_home="1", phone_mobile="1", phone_work="1", phone_fax="1", email1="test@ya.ru", email2="test@ya.com", email3="test@ya.net", homepage="test", address2="test", phone2="test", notes="test"))
    app.contact.modification_first_contact(Contact(firstname="upd1", middlename="upd1", lastname="upd1", nickname="upd1", title="upd1", company="upd1", address="upd1", phone_home="1", phone_mobile="1", phone_work="1", phone_fax="1", email1="upd1@ya.ru", email2="upd1@ya.com", email3="upd1@ya.net", homepage="www.upd1.ru", address2="upd1", phone2="upd1", notes="upd1"))