import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions

opts_chrome = ChromeOptions()
opts_firefox = FireOptions()

def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='qui'")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="By default is chrome, but you can set --browser_name='firefox'")
    parser.addoption('--browser_window_size', action='store', default="norma",
                     help="By default is norma mode, but you can set --browser_window_size='max'")

@pytest.fixture()
def browser(request):
    browser_mode = request.config.getoption("browser_mode")
    browser_name = request.config.getoption("browser_name")
    browser_window_size = request.config.getoption("browser_window_size")
    if browser_mode == "gui":
        print(f"\nbrowser_mode: {browser_mode}")
    elif browser_mode == "headless":
        opts_chrome.add_argument('--headless')
        opts_firefox.add_argument('--headless')
        print(f"\nbrowser_mode: {browser_mode}")
    else:
        print("must be gui or headless")

    if browser_name == "chrome":
        print(f"\nstart {browser_name} browser for test..")
        opts_chrome.add_argument('window_size=1200, 800')
        browser = webdriver.Chrome(options=opts_chrome)
    elif browser_name == "firefox":
        print(f"\nstart {browser_name} browser for test..")
        opts_firefox.add_argument('--width=1200')
        opts_firefox.add_argument('--height=800')
        browser = webdriver.Firefox(options=opts_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    #
    # if browser_window_size == "max":
    #     browser.maximize_window()
    # elif browser_window_size == "norma":
    #     browser.set_window_size(1200, 800)
    # else:
    #     print("must be max or norma")

    yield browser
    print("\nquit browser..")
    browser.quit()

# pytest -s -v
# pytest -s -v --browser_name="firefox"
# pytest -s -v --browser_mode="gui"
# pytest -s -v --browser_window_size="max"
# pytest -s -v --browser_name="firefox" --browser_mode="gui"
# pytest -s -v --browser_name="firefox" --browser_window_size="max"
# pytest -s -v --browser_mode="gui" --browser_window_size="max"
# pytest -s -v --browser_name="firefox" --browser_mode="gui" --browser_window_size="max"





