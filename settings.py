# -*- coding: utf-8 -*-
# Auth data
login = "aokunev"
password = "7777777"

# URLS
base_url = "http://handbook2-stage.uttc-usa.com"
auth_url = "/auth/login"
accounts_url = "/access/accounts"

class PageHelp:
    def __init__(self, wd):
        self.wd = wd

    def check_element_by_xpath(self, xpath):
        return len(self.wd.find_elements_by_xpath(xpath)) > 0

    def clickSaveButton(self):
        self.wd.find_element_by_css_selector("button.save").click()

    def fullTextSearch(self, text):
        self.wd.find_element_by_xpath("//input[@placeholder='Search']").click()
        self.wd.find_element_by_xpath("//input[@placeholder='Search']").clear()
        self.wd.find_element_by_xpath("//input[@placeholder='Search']").send_keys(text)
        if self.check_element_by_xpath("//a[@class='show-advanced rotate']"):
            self.wd.find_element_by_xpath("//a[@class='show-advanced rotate']").click()
        self.wd.find_element_by_xpath("//button[@class='search']").click()

