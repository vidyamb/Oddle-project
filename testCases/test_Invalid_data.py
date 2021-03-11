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
            assert False
        print("Now click on Donate $5 button")
        self.Dt.ClickOnDonateButton()
        payment_page_title1 = self.driver.title
        print(payment_page_title1)

        print("user can fill card details now")

        self.cp = Pasha_page(self.driver)
        self.cp.Enter_EmailID(self.email)
        print("error shown: 'Your email is incomplete.'")
        self.cp.Enter_card_Number(self.cardNum)
        print("error shown: 'Your card number is incomplete.'")
        self.driver.find_element_by_id(self.cp.CardNum_TF_ID).clear()
        self.cp.Enter_card_Number(self.Cnum)
        self.cp.Enter_ExpiryDate(self.expiryDate)
        print("error shown: 'Your card's expiration year is invalid.'")
        self.driver.find_element_by_xpath(self.cp.ExpireDate_TF_xpath).clear()
        self.cp.Enter_ExpiryDate(self.edate)
        self.cp.Enter_CVC(self.CVC)
        print("error shown: 'Your card's security code is incomplete.'")
        self.cp.Enter_Name(self.Name)
        self.cp.Click_Pay()
        if actual_title == "Stripe Checkout Sample":
            print("Above entered details are invalid")
            assert True
        else:
            assert False
        self.driver.close()

