class Pasha_page:
    Email_TF_CSS = "#email"
    CardNum_TF_ID = "cardNumber"
    ExpireDate_TF_xpath = "//div[@id='cardNumber-fieldset']//span/input[@id='cardExpiry']"
    CardCVC_TF_xpath = "//div[@id='cardNumber-fieldset']//span/input[@id='cardCvc']"
    CardName_TF_xpath = "//div[@class='FormFieldGroup-Fieldset']//span/input[@id='billingName']"
    Country_xpath = "//select[@id='billingCountry']"
    Button_Pay = "//div[@class='SubmitButton-IconContainer']"
    Check_message = "//div[@class='sr-payment-summary completed-view']/h1"
    email_error_xpath = "(//div//span[@role='alert'])[1]"
    card_error_xpath = "(//div//span[@role='alert'])[2]"
    exprirydate_error_xpath = "(// div[@ id='cardNumber-fieldset'] // span)[15]"
    cvc_error_xpath = "(//div[@id='cardNumber-fieldset']//span)[15]"

    def __init__(self, driver):
        self.driver = driver

    def Enter_EmailID(self, email_id):
        self.driver.find_element_by_css_selector(self.Email_TF_CSS).send_keys(email_id)

    def Enter_card_Number(self, cardnum):
        self.driver.find_element_by_id(self.CardNum_TF_ID).send_keys(cardnum)

    def Enter_ExpiryDate(self,expDate):
        self.driver.find_element_by_xpath(self.ExpireDate_TF_xpath).send_keys(expDate)

    def Enter_CVC(self,cvc):
        self.driver.find_element_by_xpath(self.CardCVC_TF_xpath).send_keys(cvc)


    def Enter_Name(self, name):
        self.driver.find_element_by_xpath(self.CardName_TF_xpath).send_keys(name)

    def Enter_country(self, country):
        self.driver.find_element_by_xpath(self.Country_xpath)

    def Click_Pay(self):
        self.driver.find_element_by_xpath(self.Button_Pay).click()

    def getMessage(self):
        self.message = self.driver.find_element_by_xpath(self.Check_message).text
        print(self.message)

    def checkEmailError(self):
        self.driver.find_element_by_xpath(self.email_error_xpath).is_displayed()

    def checkCardError(self):
        self.driver.find_element_by_xpath(self.card_error_xpath).is_displayed()

    def checkExpire_dateError(self):
        self.driver.find_element_by_xpath(self.exprirydate_error_xpath).is_displayed()

    def checkCVCError(self):
        self.driver.find_element_by_xpath(self.cvc_error_xpath).is_displayed()




