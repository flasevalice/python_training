from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_full_contact_info(self, contact):
        wd = self.app.wd
        self.to_add_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contacts(contact)
        self.fill_phones(contact)
        self.fill_personal_info(contact)
        self.fill_dates(contact)
        self.fill_secondary_info(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.to_home_page()

    def fill_contacts(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def fill_phones(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

    def fill_personal_info(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)

    def fill_dates(self, contact):
        wd = self.app.wd
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def fill_secondary_info(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def to_add_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php")
