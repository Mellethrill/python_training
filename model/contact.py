from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, phone_home=None,
                       phone_mobile=None, phone_work=None, phone_fax=None, email1=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

