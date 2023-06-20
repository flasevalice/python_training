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
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def fill_phones(self, contact):
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

    def fill_personal_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def fill_dates(self, contact):
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_secondary_info(self, contact):
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def to_add_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php")

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        self.first_edit()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()

    def first_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']")
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        self.first_edit()
        self.fill_contacts(new_contact_data)
        self.fill_phones(new_contact_data)
        self.fill_personal_info(new_contact_data)
        self.fill_dates(new_contact_data)
        self.fill_secondary_info(new_contact_data)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        self.to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
