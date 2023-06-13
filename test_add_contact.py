# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contacts import Contacts


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=r'D:\tools\geckodriver.exe')
        self.wd.implicitly_wait(130)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.to_add_contact_page(wd)
        self.fill_full_contact_info(wd,
                                    Contacts("n1", "mn1", "ln1", "nik1", "D:\Lol\Снимок3.png", "t1", "comp1", "addr1",
                                             "1111111", "222222", "33333", "444444",
                                             "test@mail.ru", "test2@mail.ru", "test3@mail.ru", "http://test.ru",
                                             "1", "January", "1970", "2", "February", "1980",
                                             "addr2", "454545454", "note1"))
        self.to_home_page(wd)
        self.logout(wd)

    def fill_full_contact_info(self, wd, contacts):
        wd.find_element_by_link_text("add new").click()
        self.fill_contacts(wd, contacts)
        self.fill_phones(wd, contacts)
        self.fill_personal_info(wd, contacts)
        self.fill_dates(wd, contacts)
        self.fill_secondary_info(wd, contacts)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contacts(self, wd, contacts):
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)

    def fill_phones(self, wd, contacts):
        wd.find_element_by_name("home").send_keys(contacts.home)
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        wd.find_element_by_name("work").send_keys(contacts.work)
        wd.find_element_by_name("fax").send_keys(contacts.fax)

    def fill_personal_info(self, wd, contacts):
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("photo").send_keys(contacts.photo)
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").send_keys(contacts.address)

    def fill_dates(self, wd, contacts):
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
        wd.find_element_by_name("byear").send_keys(contacts.byear)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)

    def fill_secondary_info(self, wd, contacts):
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        wd.find_element_by_name("notes").send_keys(contacts.notes)

    def to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def to_add_contact_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True


if __name__ == "__main__":
    unittest.main()
