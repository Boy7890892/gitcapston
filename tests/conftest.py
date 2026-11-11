import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    
    # TAMBAHKAN BARIS INI DI SINI:
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)
    yield driver
    # driver.quit()  # Jangan lupa komen/hapus baris quit jika ingin browser tetap terbuka setelah tes selesai