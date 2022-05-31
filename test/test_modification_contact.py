from model.contact import Contact
import random


def test_modification_random_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", phone_home="1", phone_mobile="1", phone_work="1", phone_fax="1", email1="test@ya.ru", email2="test@ya.com", email3="test@ya.net", homepage="test", address2="test", phone2="test", notes="test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="modify", middlename="modify", lastname="modify")
    random_contact = random.choice(old_contacts)
    index = old_contacts.index(random_contact)
    contact.id = old_contacts[index].id
    app.contact.modification_contact_by_id(random_contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
