# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Denis", middlename="Alex", lastname="Ratkevich", nickname="Mels", title="Title1", company="Cryptex", address="213231 AVS 21", phone_home="12345678",
                            phone_mobile="87654321", phone_work="11-11", phone_fax="22-22", email1="123@ya.ru", email2="321@ya.com", email3="231@ya.net", homepage="www.123.ru", address2="123342 sdf @@", phone2="123345", notes="done?")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
