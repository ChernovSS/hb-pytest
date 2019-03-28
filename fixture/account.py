# -*- coding: utf-8 -*-
from model.account import Account
import settings
import re


class AccountHelper(settings.PageHelp):

    def __init__(self, app, wd):
        self.app = app
        self.wd = self.app.wd

    # open accounts url
    def open_accounts_url(self):
        wd = self.app.wd
        wd.get(settings.base_url + settings.accounts_url)

    def create(self, account):
        wd = self.app.wd
        # init create
        wd.find_element_by_link_text("Create Account").click()
        # fill account form
        self.fill_account_form(account)
        # submit form
        self.clickSaveButton()
        self.app.open_home_page()

    # Change field by name
    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    # Change field dropdown
    def change_field_useruri(self, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_xpath("//span[@id='select2-account-corporationEmployee-uri-container']").click()
            wd.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(value)
            wd.find_element_by_xpath("//ul[@class='select2-results__options']/li[@aria-selected='false']").click()

    # Fill_account form
    def fill_account_form(self, account):
        self.change_field_value("Account[username]", account.username)
        self.change_field_value("Account[email]", account.email)
        self.change_field_useruri(account.emplyeeuri)

    # get list
    def get_account_list(self, account):
        wd = self.app.wd
        self.fullTextSearch(account.username)
        account_list = []
        try:
            table = wd.find_element_by_xpath(
                "//table[@class='kv-grid-table table table-bordered table-striped kv-table-wrap']")
            rows_account = table.find_elements_by_xpath(".//tbody/tr")
            for row in rows_account[:-1]:
                username = row.find_element_by_xpath(".//td[@class='username']").text
                email = row.find_element_by_xpath(".//td[@class='email']").text
                employee_uri = row.find_element_by_xpath(".//td[@class='corporationEmployee']").text
                is_enable = row.find_element_by_xpath(".//td[@class='isEnabled']").text
                account_list.append(
                            Account(username=username, email=email, emplyeeuri=employee_uri, isenable=is_enable))
        except Exception as e:
            print("error in get account list" + str(e))
        finally:
            return account_list
