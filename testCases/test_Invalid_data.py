import self

from PageObjects.CardPaymentPage import Pasha_page
from PageObjects.DonationPage import Donate
from Utilities.CustomLogger import LogGen


class Test_02_Payment:
    baseURL = "https://stripe-samples.github.io/github-pages-stripe-checkout//"
    email = "vishesham@"
    cardNum = "4000000000003QQQ"
    Cnum = '4242424242424242'
    expiryDate = 1199
    edate = "1025"
    CVC = 40
    Name = "Vish000000000003QQQesh"

    def test_With_invalid_data(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        print("Title of page is Stripe Checkout Sample")

        self.Dt = Donate(self.driver)

        if actual_title == "Stripe Checkout Sample":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_With_invalid_data.png")
            assert False
        print("Now click on Donate $5 button")
        self.Dt.ClickOnDonateButton()
        payment_page_title1 = self.driver.title
        print(payment_page_title1)

        print("user can fill card details now")

        self.cp = Pasha_page(self.driver)
        self.cp.Enter_EmailID(self.email)
        if self.cp.checkEmailError():
            print("error shown: 'Your email is incomplete.'")
        else:
            print("Email validation not available")
        self.cp.Enter_card_Number(self.cardNum)
        if self.cp.checkCardError():
            print("error shown: 'Your card number is incomplete.'")
        else:
            print("Card validation not available")
        self.driver.find_element_by_id(self.cp.CardNum_TF_ID).clear()
        self.cp.Enter_card_Number(self.Cnum)

        self.cp.Enter_ExpiryDate(self.expiryDate)
        if self.driver.find_element_by_xpath("(//div//span[@role='alert'])[1]").is_displayed():
            print("error shown: 'Your card's expiration year is invalid.'")
        else:
            print("Your card's expiration validation not available")
        self.driver.find_element_by_xpath(self.cp.ExpireDate_TF_xpath).clear()
        self.cp.Enter_ExpiryDate(self.edate)

        self.cp.Enter_CVC(self.CVC)
        if self.cp.checkCVCError():
            print("error shown: 'Your card's security code is incomplete.'")
        else:
            print("Your card's security code validation not available")

        self.cp.Enter_Name(self.Name)
        self.cp.Click_Pay()

        if self.cp.checkCVCError():
            print("error shown: 'Your card's security code is incomplete.'")

        else:
            print("Your card's security code validation not available")

        self.cp.Click_Pay()
        if self.cp.getMessage().is_displayed():
            print("validation failed")
        else:
            print("validation successful ,Test passed ")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_With_invalid_data.png")
