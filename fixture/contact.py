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
        self.contact_cache = None


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
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def modification_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # select random contact
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()
        # fill contact
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def modification_first_contact(self):
        self.modification_contact_by_index(0)

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_link_text("Select all")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = element.find_element_by_css_selector("tr > td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("tr > td:nth-child(3)").text
                self.contact_cache.append(Contact(id=id, lastname=last_name, firstname=first_name))
        return list(self.contact_cache)


