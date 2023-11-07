from selenium.webdriver.common.by import By


class BasePageLocators:
    # HEADER
    O_NAS = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/o-nas']")
    PAYMENT_DELIVERY = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/oplata-dostavka']")
    CONTACTS = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/contacts']")
    LANGUAGE_UKR = (By.XPATH, "//span[text()='Укр']")
    LANGUAGE_RUS = (By.XPATH, "//a[text()='Рус']")
    SEARCH_INPUT = (By.XPATH, "//div[@class='search-wrapper']//input[@class='form-control']")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='search-wrapper']//button[@class='btn btn-default']")
    LOGO_KS = (By.XPATH, "//img[@src='https://knigosklad.com.ua/media/logo_ks.png']")
    CONTACTS1 = (By.XPATH, "//a[text()='050-057-50-97']")
    CONTACTS2 = (By.XPATH, "//a[text()='096-217-40-10']")
    CONTACTS3 = (By.XPATH, "//a[text()='093-113-51-46']")
    CALLBACK = (By.XPATH, "//a[@id='callback-button']")
    CONTACTS_ICON = (By.XPATH, "//i[@class='fa fa-phone']")
    LOGIN_SIGNUP_ICON = (By.XPATH, "//i[@class='fa fa-user']")
    LOGIN_SIGNUP = (
        By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/customer/account/login/referer/aHR0cHM6Ly9rbmlnb3NrbGFkLmNvbS51YS91YS8,/']")
    CART_ICON = (By.XPATH, "//div[@class='cart-wrapper']//a[@class='top-cart-icon']")
    CART = (By.XPATH, "//div[@class='cart-wrapper']//span[@class='cart-qty']")

    # FOOTER
    LOGO_KS_MINI_FOOTER = (
        By.XPATH, "//footer[@id='footer']//img[@src='https://knigosklad.com.ua/media/wysiwyg/logo_ks_mini.png']")
    SUBSCRIBED_FOOTER = (By.XPATH, "//span[text()='Розсилка']")
    SUBSCRIBED_LABEL_FOOTER = (
        By.XPATH, "//label[text()='Підпишіться, щоб бути в курсі нових надходжень і спеціальних пропозицій']")
    SUBSCRIBED_EMAIL_FOOTER = (By.XPATH, "//input[@name='email']")
    SUBSCRIBED_BUTTON_FOOTER = (By.XPATH, "//button[@title='Підписатись']")
    O_NAS_FOOTER = (By.XPATH, "//footer[@id='footer']//a[@href='https://knigosklad.com.ua/ua/o-nas']")
    PAYMENT_DELIVERY_FOOTER = (
        By.XPATH, "//footer[@id='footer']//a[@href='https://knigosklad.com.ua/ua/oplata-dostavka']")
    CONTACTS_FOOTER = (By.XPATH, "//footer[@id='footer']//a[@href='https://knigosklad.com.ua/ua/contacts']")
    OFFER_FOOTER = (By.XPATH, "//footer[@id='footer']//a[@href='https://knigosklad.com.ua/ua/offer']")
    POLICY_FOOTER = (By.XPATH, "//footer[@id='footer']//a[@href='https://knigosklad.com.ua/ua/policy']")

    ADDRESS_FOOTER = (By.XPATH, "//address[text()='© 2023 КнигоСклад']")
    MADE_IN_FOOTER = (By.XPATH, "//div[@class='pull-right made-in']")


class MainPageLocators:
    # BODY
    FICTION_LITERATURE = (
        By.XPATH, "//div[@class='wrapper-menu clearfix aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja']")
    HISTORICAL_LITERATURE = (
        By.XPATH, "//div[@class='wrapper-menu clearfix aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura']")
    HISTORICAL_NOVELS = (
        By.XPATH, "//div[@class='wrapper-menu clearfix aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura/istoricheskie-romany']")

    SLIDE_MENU_1 = (By.XPATH, "//li[@data-link='detskaja/hudozhestvennaja']")
    SLIDE_MENU_2 = (By.XPATH, "//li[@data-link='obrazovanie/srednjaja-shkola/vneklassnoe-chtenie']")
    SLIDE_MENU_3 = (By.XPATH, "//li[@data-link='gifts']")
    SLIDE_MENU_4 = (By.XPATH, "//li[@data-link='obrazovanie/inostrannye-jazyki']")
    SLIDE_MENU_5 = (By.XPATH, "//li[@data-link='/hudozhestvennaja']")
    SLIDE_MENU_6 = (By.XPATH, "//li[@data-link='delovaja']")
    SLIDE_MENU_7 = (By.XPATH, "//li[@data-link='kartiny-po-nomeram']")
    SLIDE_MENU_8 = (By.XPATH, "//li[@data-link='stationery']")
    SLIDE_MENU_9 = (By.XPATH, "//li[@data-link='stationery/igrushki-sklad']")

    NOVELTY_TEXT = (By.XPATH, "//h2[text()='Новинки']")
    NOVELTY_BOOKS_3 = (
        By.XPATH, "//div[@class='product-name']//a[@href='https://knigosklad.com.ua/ua/bridzhertoni-gercog-i-ja-ukr']")

    BESTSELLERS_TEXT = (By.XPATH, "//div[text()='Бестселери']")
    BESTSELLERS_BOOKS_2 = (
        By.XPATH, "//div[@class='product-name']//a[@href='https://knigosklad.com.ua/ua/peremagati-ukrains-koju-pro-movu-nenavisti-j-ljubovi-kn-3-m']")

    POPULAR_CATEGORIES_TEXT = (By.XPATH, "//div[text()='Популярні категорії']")
    POPULAR_CATEGORIES_2 = (By.XPATH, "//a[text()='Освіта']")
    POPULAR_CATEGORIES_2_TEXT = (
        By.XPATH, "//span[text()='Навчальні посібники, енциклопедії, словники, решітки, прописи — все, що потрібно школярам, абітурієнтам та студентам']")

    READ_TOGETHER = (By.XPATH, "//h2[text()='Читайте разом із Книгоскладом!']")
