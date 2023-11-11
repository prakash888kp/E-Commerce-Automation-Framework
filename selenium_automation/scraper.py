import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_amazon():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")  # Replace with the desired product search URL
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox').send_keys('Hindi Books') # Replace with your desired keyword
    driver.find_element(By.ID, 'nav-search-submit-button').click()
    time.sleep(10)

    # Extract and store the name, price, and rating in a CSV file
    products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')

    with open('data/scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, 'h2 a span').text
                price = product.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                rating = product.find_element(By.CSS_SELECTOR, '[aria-label*="out of 5 stars"]').get_attribute('aria-label')
                writer.writerow([name, price, rating])
            except:
                pass

    driver.quit()