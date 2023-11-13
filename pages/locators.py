from selenium.webdriver.common.by import By


class BasePageLocators:
    # HEADER
    O_NAS = (By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/o-nas']")
    PAYMENT_DELIVERY = (
        By.XPATH, "//div[@class='top-block-2']//a[@href='https://knigosklad.com.ua/ua/oplata-dostavka']")
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
        By.XPATH,
        "//a[@href='https://knigosklad.com.ua/ua/customer/account/login/referer/aHR0cHM6Ly9rbmlnb3NrbGFkLmNvbS51YS91YS8,/']")
    CART_ICON = (By.XPATH, "//div[@class='cart-wrapper']//a[@class='top-cart-icon']")
    CART = (By.XPATH, "//div[@class='cart-wrapper']//span[@class='cart-qty']")

    CATALOG_SCROLLING = (By.XPATH, "//header[@id='sticky-header']//span[@class='catalog-menu-text']")
    CATALOG_BUTTON_SCROLLING = (
        By.XPATH, "//header[@id='sticky-header']//div[@class='pull-left']//button[@type='button']")
    FICTION_LITERATURE_SCROLLING = (
        By.XPATH,
        "//div[@class='pull-left top-menu aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja']")
    HISTORICAL_LITERATURE_SCROLLING = (
        By.XPATH,
        "//div[@class='pull-left top-menu aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura']")
    HISTORICAL_NOVELS_SCROLLING = (
        By.XPATH,
        "//div[@class='pull-left top-menu aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura/istoricheskie-romany']")
    LOGO_SCROLLING = (By.XPATH, "//header[@id='sticky-header']//span[@class='logo']")
    SEARCH_BUTTON_SCROLLING = (By.XPATH, "//header[@id='sticky-header']//div[@class='search-button']")
    CART_SCROLLING = (By.XPATH, "//header[@id='sticky-header']//a[@class='top-cart-icon']")
    CART_COUNT_SCROLLING = (By.XPATH, "//header[@id='sticky-header']//span[@class='cart-qty']")

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
        By.XPATH,
        "//div[@class='wrapper-menu clearfix aside-nav']//a[@class='level-top']//span[text()='Художня література']")
    HISTORICAL_LITERATURE = (
        By.XPATH,
        "//div[@class='wrapper-menu clearfix aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura']")
    HISTORICAL_NOVELS = (
        By.XPATH,
        "//div[@class='wrapper-menu clearfix aside-nav']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura/istoricheskie-romany']")

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
        By.XPATH, "//div[@id='home-slider-1326']//div[@class='owl-wrapper']//li[3]//div[@class='product-name']")

    BESTSELLERS_TEXT = (By.XPATH, "//div[text()='Бестселери']")
    BESTSELLERS_BOOKS_2 = (
        By.XPATH, "//div[@id='home-slider-7212']//div[@class='owl-wrapper']//li[3]//div[@class='product-name']")

    POPULAR_CATEGORIES_TEXT = (By.XPATH, "//div[text()='Популярні категорії']")
    POPULAR_CATEGORIES_2 = (By.XPATH, "//a[text()='Освіта']")
    POPULAR_CATEGORIES_2_TEXT = (
        By.XPATH,
        "//span[text()='Навчальні посібники, енциклопедії, словники, решітки, прописи — все, що потрібно школярам, абітурієнтам та студентам']")

    READ_TOGETHER = (By.XPATH, "//h2[text()='Читайте разом із Книгоскладом!']")


class SignupLoginPageLocators:
    LOGIN_TEXT = (By.XPATH, "//h3[text()='Вхід']")
    LOGIN_PUSH = (By.XPATH, "//div[@class='page-title clearfix']//a[text()='Вхід']")
    LOGIN_EMAIL_TEXT = (By.XPATH, "//label[@for='email']")
    LOGIN_EMAIL = (By.XPATH, "//input[@name='login[username]']")
    LOGIN_PASSWORD_TEXT = (By.XPATH, "//label[@for='pass']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='login[password]']")
    REMEMBER_ME = (By.XPATH, "//li[@id='remember-me-box-login']//input[@name='persistent_remember_me']")
    LOGIN = (By.XPATH, "//span[text()='Вхід']")
    FORGOT_PASS = (By.XPATH, "//a[text()='Забули пароль?']")

    SIGNUP = (By.XPATH, "//a[text()='Зареєструватись']")
    PERSONAL_INFO = (By.XPATH, "//h3[text()='Персональна інформація']")
    FIRSTNAME_TEXT = (By.XPATH, "//label[@for='firstname']")
    FIRSTNAME = (By.XPATH, "//input[@name='firstname']")
    LASTNAME_TEXT = (By.XPATH, "//label[@for='lastname']")
    LASTNAME = (By.XPATH, "//input[@name='lastname']")
    EMAIL_TEXT = (
        By.XPATH, "//form[@action='https://knigosklad.com.ua/ua/customer/account/createpost/']//label[text()='E-mail']")
    EMAIL = (
        By.XPATH, "//form[@action='https://knigosklad.com.ua/ua/customer/account/createpost/']//input[@name='email']")
    SUBSCRIBED_CHECKBOX = (By.XPATH, "//input[@name='is_subscribed']")
    SUBSCRIBED_TEXT = (By.XPATH, "//label[@for='is_subscribed']")
    PASSWORD_TITLE = (By.XPATH, "//h3[text()='Пароль']")
    PASSWORD_TEXT = (By.XPATH, "//label[@for='password']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    PASSWORD_CONFIRM_TEXT = (By.XPATH, "//label[@for='confirmation']")
    PASSWORD_CONFIRM = (By.XPATH, "//input[@id='confirmation']")
    REMEMBERME_CHECKBOX = (By.XPATH, "//li[@id='remember-me-box-register']//input[@class='checkbox']")
    REMEMBERME_TEXT = (By.XPATH, "//label[@for='remember_meRjf64EvMct']")
    SIGNUP_BUTTON = (By.XPATH, "//span[text()='Зареєструватись']")

    CLOSE_BUTTON = (By.XPATH, "//div[@class='login-wrapper']//div[@class='close-popup']")

    REGISTER_SUCCESSFUL = (By.XPATH, "//div[@id='window-overlay-register']")
    LOGIN_SUCCESSFUL = (By.XPATH, "//div[@id='window-overlay-login']")


class CabinetPageLocators:
    USER_BUTTON = (By.XPATH, "//span[@class='user-icon']")
    LINK_ACCOUNT = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/customer/account/']")
    LINK_WISHLIST = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/wishlist/']")
    LINK_CHECKOUT = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/checkout/']")
    LOGOUT = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/customer/account/logout/']")
    TITLE_ACCOUNT = (By.XPATH, "//h1[text()='Моя робоча область']")
    WELCOME_TEXT = (By.XPATH, "//h3[@class='hello panel-title']")
    ACCOUNT_INFO = (By.XPATH, "//h2[text()='Інформація по аккаунту']")
    CONTACT_INFO = (By.XPATH, "//h3[text()='Контактна інформація']")
    INFO_LETTER = (By.XPATH, "//h3[text()='Інформаційні листи']")
    ADDRESS = (By.XPATH, "//h2[text()='Адресна книга']")
    DEFAULT_PAYMENT = (By.XPATH, "//h3[text()='Адреса оплати за замовчуванням']")
    DEFAULT_ADDRESS = (By.XPATH, "//h3[text()='Адреса доставки За замовчуванням']")
    MY_ACCOUNT = (By.XPATH, "//span[text()='Мій аккаунт']")
    INFO = (By.XPATH, "//li[@class='current']")
    INFO_ACCOUNT = (By.XPATH, "//a[text()='Інформація по аккаунту']")
    ADDRESS_BOOK = (By.XPATH, "//a[text()='Адресна книга']")
    SUBSCRIBED_NEWS = (By.XPATH, "//a[text()='Підписки на новини']")
    MY_REVIEWS = (By.XPATH, "//a[text()='Мої відгуки про товари']")
    MY_ORDERS = (By.XPATH, "//a[text()='Мої замовлення']")


class CategoryPageLocators:
    HISTORICAL_LITERATURE = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura']")
    PROSE = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/proza']")
    CLASSIC = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/klassika']")
    NOVELS = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/romany']")
    UKRAINIAN = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/ukrains_ka']")
    ENGLISH = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/anglijs_ka']")
    COLLECTION = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/proza/sobranie-sochinenij']")
    MODERN = (
        By.XPATH,
        "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/proza/sovremennaja']")
    BOOK_2 = (
        By.XPATH, "//ul[@class='products-grid row three-columns first last odd']//li[2]//div[@class='product-name']")
    PAGE_1_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[1]")
    PAGE_2_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[2]")
    PAGE_3_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[3]")
    PAGE_4_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[4]")
    PAGE_5_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[5]")
    PAGE_NEXT_CATEGORY = (By.XPATH, "//div[@class='category-products']/div[1]//div[@class='pager']//li[6]")
    PAGE_1_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[1]")
    PAGE_2_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[2]")
    PAGE_3_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[3]")
    PAGE_4_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[4]")
    PAGE_5_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[5]")
    PAGE_NEXT_CATEGORY_DOWN = (By.XPATH, "//div[@class='category-products']/div[2]//div[@class='pager']//li[6]")
    SORT_NAME = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/select/option[1]")
    SORT_PRICE = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/select/option[2]")
    SORT_NEW = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/select/option[3]")
    SORT_MOST_VIEWED = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/select/option[4]")
    SORT_TEXT = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/label")
    SORT_BUTTON = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[2]/div[1]/button")
    SORT_ICON = (
        By.XPATH, "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/a")
    ARTICLE = (By.XPATH, "//div[@class='seo_article']")
    ON_PAGE = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/label")
    ON_PAGE_BUTTON = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/div[1]/button")
    ON_PAGE_20 = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[1]")
    ON_PAGE_40 = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[2]")
    ON_PAGE_80 = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[3]")
    ON_PAGE_160 = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[4]")


class OrderPageLocators:
    ORDER = (By.XPATH, "//div[@class='page-title']")
    NAME = (By.XPATH, "//label[@for='billing:firstname']")
    NAME_INPUT = (By.XPATH, "//input[@id='billing:firstname']")
    LASTNAME = (By.XPATH, "//label[@for='billing:lastname']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='billing:lastname']")
    CITY = (By.XPATH, "//div[@id='novaposhta_cities_chosen']")
    CITY_DNIPRO = (By.XPATH, "//li[@data-option-array-index='1']")
    FREE_SHIPPING = (By.XPATH, "//input[@id='s_method_freeshipping_freeshipping']")
    TELEPHONE = (By.XPATH, "//input[@id='billing:telephone']")
    PAYMENT = (By.XPATH, "//input[@id='p_method_checkmo']")
    NOTICE = (By.XPATH, "//textarea[@id='customer_comment']")
    CHECKOUT = (By.XPATH, "//button[@class='btn btn-primary btn-checkout opc-btn-checkout']")
    MESSAGE_SUCCESSFUL = (By.XPATH, "//h1[text()='Ваше замовлення прийнято.']")
    CART_BOOK_2 = (
        By.XPATH,
        "//ul[@class='products-grid row three-columns first last odd']//li[2]//i[@class='fa fa-shopping-cart']")
    CART_SUCCESSFUL = (By.XPATH, "//div[@class='popup-text success-msg']")
    TO_ORDER = (By.XPATH, "//button[@class='btn btn-primary btn-proceed-checkout']")


class SearchPageLocators:
    RESULT = (By.XPATH, "//div[@class='page-title']")
    ON_PAGE_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/label")
    ON_PAGE_BUTTON_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/div[1]/button")
    ON_PAGE_20_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[1]")
    ON_PAGE_40_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[2]")
    ON_PAGE_80_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[3]")
    ON_PAGE_160_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[1]/div[1]/div[1]//li[4]")
    SORT_RELEVANT_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/select/option[1]")
    SORT_NAME_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/select/option[2]")
    SORT_PRICE_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/select/option[3]")
    SORT_NEW_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/select/option[4]")
    SORT_MOST_VIEWED_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/select/option[5]")
    SORT_TEXT_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/label")
    SORT_BUTTON_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/div[2]/div[1]/button")
    SORT_ICON_SEARCH = (
        By.XPATH,
        "//div[@class='category-products']/div[@class='toolbar clearfix no-pagination']/div[@class='sorter']/div/a")


class ProductPageLocators:
    BOOK_AUTHOR = (
        By.XPATH,
        "//div[@class='product-shop col-sm-6 medium-layout a-left']//a[@href='https://knigosklad.com.ua/ua/catalogsearch/result/?q=%D0%93%D0%BE%D0%BD%D1%87%D0%B0%D1%80%D0%BE%D0%B2%D0%B0+%D0%9C.']")
    BOOK_NAME = (
        By.XPATH,
        "//div[@class='product-shop col-sm-6 medium-layout a-left']//h1[text()='Чарівні абетки. Різдвяна абетка ']")
    BOOK_PRICE = (
        By.XPATH,
        "//div[@class='product-shop col-sm-6 medium-layout a-left']//div[@class='price-box']//span[@class='price']")
    BOOK_TO_CART = (By.XPATH, "//button[@id='product-addtocart-button']")
    BOOK_TO_WISHLIST = (By.XPATH, "//ul[@class='add-to-links clearfix']//i[@class='fa fa-heart']")
    BOOK_DESCRIPTION = (By.XPATH, "//div[@class='panel-title']")
    BOOK_DESCRIPTION_TEXT = (By.XPATH, "//div[@class='std']")
