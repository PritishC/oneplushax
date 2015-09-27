# -*- coding: utf-8 -*-
"""
    oneplus_invites.py

    :copyright: (C) Pritish Chakraborty
"""
import argparse
from selenium import webdriver
import time


class OnePlus:

    def __init__(self, email_base, invite_url):
        """
        Initializer
        """
        self.driver = webdriver.Chrome()
        self.email_base = email_base
        self.invite_url = invite_url

        # The following lines are needed if you decide to use Phantom.
        # Phantom didn't work for me - Chrome did.
        # Probably because of the captcha verification.
        # https://github.com/ariya/phantomjs/issues/11637
        #self.driver.set_window_size(1150, 900)
        #self.driver.set_window_position(0, 0)

    def test_oneplus_invites(self):
        """
        Test OnePlus invite spamming for Moksh.
        """
        email_domain = 'gmail.com'
        separator = '@'
        emails = [self.email_base + separator + email_domain]

        # Generate the various emails with period characters
        # in different positions
        for i in range(1, len(self.email_base)):
            emails.append(
                self.email_base[:i] + '.' + self.email_base[i:] +
                separator + email_domain
            )

        for email in emails:
            try:
                print "On email: %s" % email
                self.driver.implicitly_wait(12)
                self.driver.get(self.invite_url)
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

        self.driver.close()


parser = argparse.ArgumentParser(description='OnePlus Hax')
parser.add_argument(
    '--email_base', required=True,
    help='Base of email. Eg: abc if email is abc@gmail.com'
)
parser.add_argument(
    '--invite-url', required=True,
    help='One Plus Invite URL. Encapsulate in double quotes.'
)

args = parser.parse_args()

OnePlus(email_base=args.email_base, invite_url=args.invite_url).test_oneplus_invites()
