from model.contact import Contact
from random import randrange


def test_modification_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", phone_home="1", phone_mobile="1", phone_work="1", phone_fax="1", email1="test@ya.ru", email2="test@ya.com", email3="test@ya.net", homepage="test", address2="test", phone2="test", notes="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modify", middlename="modify", lastname="modify")
    contact.id = old_contacts[index].id
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
