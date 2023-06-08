# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from personal_info import PersonalInfo
from phones import Phones
from contacts import Contacts
from dates import Dates
from secondary_info import SecondaryInfo


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
        self.fill_full_contact_info(wd)
        self.to_home_page(wd)
        self.logout(wd)

    def fill_full_contact_info(self, wd):
        wd.find_element_by_link_text("add new").click()
        self.fill_personal_info(wd, PersonalInfo("n1", "mn1", "ln1", "nik1", "D:\Lol\Снимок3.png", "t1", "comp1", "addr1"))
        self.fill_phones(wd, Phones("1111111", "222222", "33333", "444444"))
        self.fill_contacts(wd, Contacts("test@mail.ru", "test2@mail.ru", "test3@mail.ru", "http://test.ru"))
        self.fill_dates(wd, Dates("1", "January", "1970", "2", "February", "1980"))
        self.fill_secondary_info(wd, SecondaryInfo("addr2", "454545454", "note1"))
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_secondary_info(self, wd, secondary_info):
        wd.find_element_by_name("address2").send_keys(secondary_info.address2)
        wd.find_element_by_name("phone2").send_keys(secondary_info.phone2)
        wd.find_element_by_name("notes").send_keys(secondary_info.notes)

    def fill_dates(self, wd, dates):
        Select(wd.find_element_by_name("bday")).select_by_visible_text(dates.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(dates.bmonth)
        wd.find_element_by_name("byear").send_keys(dates.byear)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(dates.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(dates.amonth)
        wd.find_element_by_name("ayear").send_keys(dates.ayear)

    def fill_contacts(self, wd, contacts):
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)

    def fill_phones(self, wd, phones):
        wd.find_element_by_name("home").send_keys(phones.home)
        wd.find_element_by_name("mobile").send_keys(phones.mobile)
        wd.find_element_by_name("work").send_keys(phones.work)
        wd.find_element_by_name("fax").send_keys(phones.fax)

    def fill_personal_info(self, wd, pers_info):
        wd.find_element_by_name("firstname").send_keys(pers_info.firstname)
        wd.find_element_by_name("middlename").send_keys(pers_info.middlename)
        wd.find_element_by_name("lastname").send_keys(pers_info.lastname)
        wd.find_element_by_name("nickname").send_keys(pers_info.nickname)
        wd.find_element_by_name("photo").send_keys(pers_info.photo)
        wd.find_element_by_name("title").send_keys(pers_info.title)
        wd.find_element_by_name("company").send_keys(pers_info.company)
        wd.find_element_by_name("address").send_keys(pers_info.address)

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
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()
