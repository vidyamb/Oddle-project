from selenium.webdriver import ActionChains

from PageObjects.CardPaymentPage import Pasha_page
from PageObjects.DonationPage import Donate
from Utilities.CustomLogger import LogGen


class Test_05_Payment:
    baseURL = "https://stripe-samples.github.io/github-pages-stripe-checkout//"
    email = "vmessi@gmail.com"
    cardNum = 4000000000003220
    expiryDate = 626
    CVC = 879
    Name = "LionelMessi"

    def test_3D_secure(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        print("Title of page is Stripe Checkout Sample")

        self.Dt = Donate(self.driver)

        if actual_title == "Stripe Checkout Sample":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_3D_secure.png")
            assert False
        print("Now click on Donate $5 button")
        self.Dt.ClickOnDonateButton()
        payment_page_title1 = self.driver.title
        print(payment_page_title1)

        print("user can fill card details now")
        self.driver.find_element_by_xpath("//div//input[@id='email']").send_keys("vidyavidu@gmail.com")
        self.cp = Pasha_page(self.driver)
        # self.cp.Enter_EmailID(self.email)
        self.cp.Enter_card_Number(self.cardNum)
        self.cp.Enter_ExpiryDate(self.expiryDate)
        self.cp.Enter_CVC(self.CVC)
        self.cp.Enter_Name(self.Name)
        self.cp.Click_Pay()

        # {----AFTER PAY CLICK , UNABLE TO SWITCH TO IFRAME----,following are the further code..}

        # self.driver.find_element_by_css_selector("button#test-source-authorize-3ds").click()
        # iframe = self.driver.find_element_by_xpath("//iframe[@name='stripe-challenge-frame']")
        # self.driver.switch_to.frame(iframe)
        # print("switched to frame")

        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # print("scrolled down")
        # self.button = self.driver.find_element_by_xpath("(//form[@class='ActionForm']//button)[2]")
        # print(self.button.is_displayed())
        # self.button.click()
        # print("clicked on complete button")
        # self.cp.getMessage()
        # if self.cp.message == "Your test payment succeeded":
        # self.driver.save_screenshot(".\\Screenshots\\" + "test_3D_secure.png")
        # print("3D Secure Payment Successful ,Screenshot captured")
        # else:
        # self.driver.save_screenshot(".\\Screenshots\\" + "test_3D_secure.png")
        # print("Payment failed")
        self.driver.close()
