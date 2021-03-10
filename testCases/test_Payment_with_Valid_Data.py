import pytest
from selenium import webdriver


from PageObjects.CardPaymentPage import Pasha_page
from PageObjects.DonationPage import Donate
from Utilities.CustomLogger import LogGen
class Test_01_Payment:
    baseURL = "https://stripe-samples.github.io/github-pages-stripe-checkout//"
    email = "vidyavidu213@gmail.com"
    cardNum = 4242424242424242
    expiryDate= 525
    CVC = 456
    Name = "Vidya"

    def test_positive_flow(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        print("Title of page is Stripe Checkout Sample")

        self.Dt = Donate(self.driver)

        if actual_title == "Stripe Checkout Sample":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Without_3D_secure_Verfication.png")
            assert False
        print("Now click on Donate $5 button")
        self.Dt.ClickOnDonateButton()
        payment_page_title1 = self.driver.title
        print(payment_page_title1)

        print("user can fill card details now")
        self.driver.find_element_by_xpath("//div//form//div//span/input[@id='email']").send_keys("vidyavidu@gmail.com")
        self.cp = Pasha_page(self.driver)
        #self.cp.Enter_EmailID(self.email)
        self.cp.Enter_card_Number(self.cardNum)
        self.cp.Enter_ExpiryDate(self.expiryDate)
        self.cp.Enter_CVC(self.CVC)
        self.cp.Enter_Name(self.Name)
        self.cp.Click_Pay()
        self.cp.getMessage()
        if self.cp.message == "Your test payment succeeded":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Without_3D_secure_Verfication.png")
            print("payment done successfull,Screenshot captured")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Without_3D_secure_Verfication.png")
            print("Payment failed")









