# -*- coding: utf-8 -*-
"""
    oneplus_invites.py

    :copyright: (C) Pritish Chakraborty
"""
from selenium import webdriver
import time


class OnePlus:

    def setUp(self):
        """
        This method is called before each
        test function executes.
        """
        self.driver = webdriver.Chrome()

        # The following lines are needed if you decide to use Phantom.
        # Phantom didn't work for me - Chrome did.
        # https://github.com/ariya/phantomjs/issues/11637
        #self.driver.set_window_size(1150, 900)
        #self.driver.set_window_position(0, 0)

    def test_oneplus_invites(self):
        """
        Test OnePlus invite spamming for Moksh.
        """
        self.setUp()

        url = 'your_oneplus_invite_url'
        email_base = 'your_email'
        email_domain = 'gmail.com'
        separator = '@'
        emails = [email_base + separator + email_domain]

        # Generate the various emails with period characters
        # in different positions
        for i in range(1, len(email_base)):
            emails.append(
                email_base[:i] + '.' + email_base[i:] +
                separator + email_domain
            )

        for email in emails:
            try:
                print "On email: %s" % email
                self.driver.implicitly_wait(12)
                self.driver.get(url)
                print "On the page"

                self.driver.implicitly_wait(5)

                email_box = self.driver.find_element_by_id('email')
                email_box.send_keys(email)

                print "Typed the email"
                print "Switching to Iframe"

                self.driver.switch_to.frame(
                    self.driver.find_element_by_css_selector('.g-recaptcha')
                    .find_element_by_tag_name('iframe')
                )

                print "Ticking the box"
                self.driver.find_element_by_css_selector(
                    '.recaptcha-checkbox-checkmark'
                ).click()
                time.sleep(10)

                print "Checked the box"
                print "Switching back to normal context"

                self.driver.switch_to.default_content()

                self.driver.find_element_by_id('submit_email').click()
                print "Clicked submit"
            except Exception as e:
                print e

        self.tearDown()

    def tearDown(self):
        """
        This function is executed after each test function.
        """
        self.driver.close()


OnePlus().test_oneplus_invites()
