from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init add contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        # submit create
        wd.find_element_by_name("submit").click()


    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select edit first contact
        wd.find_element_by_css_selector("img[title='Edit']").click()
        # delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()


    def modification_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # select edit first contact
        wd.find_element_by_css_selector("img[title='Edit']").click()
        # fill contact
        self.fill_contact(contact)
        # submit modification
        wd.find_element_by_name("update").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_link_text("Select all")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contact_list = []
        for element in wd.find_elements_by_css_selector("tr[name]"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            last_name = element.find_element_by_css_selector("tr > td:nth-child(2)").text
            first_name = element.find_element_by_css_selector("tr > td:nth-child(3)").text
            contact_list.append(Contact(id=id, lastname=last_name, firstname=first_name))
        return contact_list


