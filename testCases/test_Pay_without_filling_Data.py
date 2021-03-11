from PageObjects.CardPaymentPage import Pasha_page
from PageObjects.DonationPage import Donate
from Utilities.CustomLogger import LogGen


class Test_03_Payment:
    baseURL = "https://stripe-samples.github.io/github-pages-stripe-checkout//"

    def test_with_noData_input(self, setup):
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
        self.cp.Click_Pay()
        print("REQUIRED:Please enter Email ID")
        print("REQUIRED:Please enter CARD number")
        print("REQUIRED:Please enter Name")
        print("Failed,System not allow to proceed")
        self.driver.close()
