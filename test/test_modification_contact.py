from model.contact import Contact


def test_modification_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", phone_home="1", phone_mobile="1", phone_work="1", phone_fax="1", email1="test@ya.ru", email2="test@ya.com", email3="test@ya.net", homepage="test", address2="test", phone2="test", notes="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="modify", middlename="modify", lastname="modify")
    contact.id = old_contacts[0].id
    app.contact.modification_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
