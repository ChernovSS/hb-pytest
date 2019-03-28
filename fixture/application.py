# -*- coding: utf-8 -*-
from selenium import webdriver
import settings


class Application:

    def __init__(self):
        # Start Firefox
        self.wd = webdriver.Firefox()
        # Задержка в 5 сек
        self.wd.implicitly_wait(5)

    def open_home_page(self):
        wd = self.wd
        wd.get(settings.base_url)

    def login(self):
        wd = self.wd
        try:
            wd.get(settings.base_url + settings.auth_url)
            wd.find_element_by_id("loginForm-username").send_keys(settings.login)
            wd.find_element_by_id("loginForm-password").send_keys(settings.password)
            wd.find_element_by_name("login-button").click()

        except:
            print("Can't login")

    def destroy(self):
        self.wd.quit()
