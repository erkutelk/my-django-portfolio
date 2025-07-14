import os
import time
import pytest
from selenium import webdriver
from tests.test.test_selenium.selenium_sites import SeleniumTest
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_iletisim_sayfasi(driver):
    tarih = str(int(time.time()))[:9]
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/contact'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_title', f"asdas")
    assert test_value.text_giris_islemleri('#id_konum', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_konum2', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_telefon', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_mail', f"Deneme{tarih}")
    test_value.tıklama('button')
    alert_element = test_value.driver.find_element(By.CSS_SELECTOR, '[role="alert"]')
    text_degei = alert_element.text.strip()
    try:
        assert text_degei=='Bilgiler başarıyla güncellendi.'    
        print('🟩 İletişim sayfası başarıyla güncellendi')
    except:
        print('🟥Hata meydana geldi')

        


