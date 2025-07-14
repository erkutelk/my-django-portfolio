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

def test_info_sayfası_guncelleme(driver):
    import time
    tarih = str(int(time.time()))[:9]
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/admin_info/page'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_title', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_description', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_linkedin', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_instagram', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_git', f"Deneme{tarih}")
    dosya_yolu = os.path.abspath("home/static/home/images/pexels-kyleloftusstudios-2734519.jpg")
    assert test_value.dosya_yukle('images', dosya_yolu)
    assert test_value.tıklama('button')

