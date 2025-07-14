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

def test_servis_sayfasi(driver):
    tarih = str(int(time.time()))[:9]
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/servis_ekle'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_title', f"Deneme{tarih}")
    assert test_value.text_giris_islemleri('#id_description', f"Deneme{tarih}")
    assert test_value.tıklama("#id_isActive")

    assert test_value.tıklama('button')  
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.table > tbody > tr > td:nth-child(2)'))
        )
    except:
        pytest.fail("Tablo yüklenmedi veya öğe bulunamadı!")

    tum_satirlar = test_value.driver.find_elements(By.CSS_SELECTOR, '.table > tbody > tr > td:nth-child(2)')
    
    if not tum_satirlar:
        pytest.fail("Tabloda hiç satır yok!")
    
    deger = tum_satirlar[-1].text.strip()
    print('deger:', deger)
    print('deger:', tarih)

    assert deger == f'Deneme{tarih}'
    time.sleep(5)


