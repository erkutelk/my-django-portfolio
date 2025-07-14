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

def test_hakkimizda_sayfasi(driver):
    tarih = str(int(time.time()))[:9]
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/about_page'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_about_title', f"Hakkimizda bölümü")
    assert test_value.text_giris_islemleri('#id_about_description', f"Deneme{tarih}")
    dosya_yolu = os.path.abspath("home/static/home/images/pexels-kyleloftusstudios-2734519.jpg")
    assert test_value.dosya_yukle('about_image', dosya_yolu)
    assert test_value.tıklama('button')
    


