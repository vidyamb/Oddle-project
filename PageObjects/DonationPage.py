class Donate:
    button_text = "//button[1]"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnDonateButton(self):
        self.driver.find_element_by_xpath(self.button_text).click()

