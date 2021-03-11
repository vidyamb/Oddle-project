from selenium.webdriver.common.alert import Alert

from PageObjects.CardPaymentPage import Pasha_page
from PageObjects.DonationPage import Donate
from Utilities.CustomLogger import LogGen


class Test_04_Payment:
    baseURL = "https://stripe-samples.github.io/github-pages-stripe-checkout//"
    email = "vmessi@gmail.com"
    cardNum = 4000000000003220
    expiryDate = 626
    CVC = 879
    Name = "LionelMessi"

    def test_cancel_pay(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        print("Title of page is Stripe Checkout Sample")

        self.Dt = Donate(self.driver)

        if actual_title == "Stripe Checkout Sample":
            assert True
        else:
            assert False
        print("Now click on Donate $5 button")
        self.Dt.ClickOnDonateButton()
        payment_page_title1 = self.driver.title
        print(payment_page_title1)
        print("user can fill card details now")
        self.driver.find_element_by_xpath("//div//input[@id='email']").send_keys("vidyavidu@gmail.com")
        self.cp = Pasha_page(self.driver)
        self.cp.Enter_card_Number(self.cardNum)
        self.cp.Enter_ExpiryDate(self.expiryDate)
        self.cp.Enter_CVC(self.CVC)
        self.cp.Enter_Name(self.Name)
        print("Click on back button")
        self.driver.find_element_by_xpath("//div[@class='Header-merchantLogoContainer']//span").click()
        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()
        self.cp.getMessage()
        if self.cp.message == "Your test payment was canceled":

            print("3D Secure Payment cancelled ")
        else:
            print("Failed to cancel payment")
        self.driver.close()