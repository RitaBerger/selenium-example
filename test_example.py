import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.smoketest
def test_amazon(browser):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    base_url="https://www.amazon.com/"
    expected_title = 'Amazon.com. Spend less. Smile more.'

    browser.get(base_url)
    assert expected_title in browser.title
    assert base_url in browser.current_url
