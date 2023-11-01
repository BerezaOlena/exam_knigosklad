from selenium.webdriver.common.by import By


class BasePageLocators:
    O_NAS = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/o - nas']")
    OPLATA_DOSTAVKA = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/oplata-dostavka']")
    CONTACTS = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/contacts']")
    LANGUAGE_UKR = (By.XPATH, "//span[text()='Укр']")
    LANGUAGE_RUS = (By.XPATH, "//span[text()='Рус']")
    SEARCH = (By.XPATH, "//input[@id='search_41']")
    LOGO_KS = (By.XPATH, "//img[@src='https://knigosklad.com.ua/media/logo_ks.png']")
    CONTACTS1 = (By.XPATH, "//a[text()='050-057-50-97']")
    CONTACTS2 = (By.XPATH, "//a[text()='096-217-40-10']")
    CONTACTS3 = (By.XPATH, "//a[text()='093-113-51-46']")
    CALLBACK_BUTTON = (By.XPATH, "//a[@id='callback-button']")
    CONTACTS_ICON = (By.XPATH, "//i[@class='fa fa-phone']")
    LOGIN_SIGNUP_ICON = (By.XPATH, "//i[@class='fa fa-user']")
    LOGIN_SIGNUP = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/customer/account"
                              "/login/referer/aHR0cHM6Ly9rbmlnb3NrbGFkLmNvbS51YS91YS8,']")
    CART_ICON = (By.XPATH, "//div[@class='cart-wrapper']//a[@class='top-cart-icon']")
    CART = (By.XPATH, "//div[@class='cart-wrapper']//span[@class='cart-qty']")
