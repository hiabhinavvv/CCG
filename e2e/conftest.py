import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Setup Chrome WebDriver"""
    options = Options()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="session")
def base_urls():
    """Return base URLs for frontend and backend"""
    return {
        'frontend': 'http://localhost:5173',
        'backend': 'http://localhost:8000'
    }
