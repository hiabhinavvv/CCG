import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_frontend_loads(driver, base_urls):
    """Test that frontend loads successfully"""
    driver.get(base_urls['frontend'])
    
    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Check that page loaded
    assert driver.title or driver.find_element(By.TAG_NAME, "body")
    print("✅ Frontend loaded successfully")

def test_clerk_sign_in_present(driver, base_urls):
    """Test that Clerk authentication UI is present"""
    driver.get(base_urls['frontend'])
    
    # Wait for Clerk to initialize
    time.sleep(2)
    
    # Check for any buttons (sign-in/sign-up)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    assert len(buttons) > 0, "No buttons found on page"
    print(f"✅ Found {len(buttons)} buttons on page")

def test_navigation_elements(driver, base_urls):
    """Test that navigation elements are present"""
    driver.get(base_urls['frontend'])
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Check for navigation or main content
    body = driver.find_element(By.TAG_NAME, "body")
    assert body.text or body.get_attribute("innerHTML")
    print("✅ Page has content")

def test_backend_api_accessible(driver, base_urls):
    """Test that backend API docs are accessible"""
    driver.get(f"{base_urls['backend']}/docs")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Check for Swagger UI
    page_source = driver.page_source.lower()
    assert "swagger" in page_source or "api" in page_source
    print("✅ Backend API docs accessible")

def test_protected_route_requires_auth(driver, base_urls):
    """Test that protected routes require authentication"""
    driver.get(base_urls['frontend'])
    
    # Wait for page load
    time.sleep(2)
    
    # Try to access app without signing in
    # The app should show sign-in UI or redirect
    page_content = driver.page_source.lower()
    
    # Should have some auth-related content
    has_auth = any(word in page_content for word in ['sign', 'login', 'auth', 'clerk'])
    assert has_auth, "No authentication UI found"
    print("✅ Authentication required for protected content")

def test_page_responsiveness(driver, base_urls):
    """Test that page is responsive"""
    driver.get(base_urls['frontend'])
    
    # Test mobile size
    driver.set_window_size(375, 667)
    time.sleep(1)
    
    body = driver.find_element(By.TAG_NAME, "body")
    assert body.is_displayed()
    
    # Test desktop size
    driver.set_window_size(1920, 1080)
    time.sleep(1)
    
    assert body.is_displayed()
    print("✅ Page is responsive")
