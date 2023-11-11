import files


import cv2
import pytesseract
import re


# Set Tesseract path (not required in Colab)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Upload the screenshot file
uploaded = files.upload()

# Access the uploaded file
file_name = list(uploaded.keys())[0]

# Read the uploaded image
img = cv2.imread(file_name)

text = pytesseract.image_to_string(img)

print(text)

import re
import csv
# Extracting product name, rating, and price

product_name_match = re.search(r'(.*?)\s*Hindi Edition', text)
product_name = product_name_match.group(1).strip() if product_name_match else 'Product Name Not Found'

rating_match = re.search(r'(\d\.\d)\s*\(\d+\)\s*.*?(\d{4})', text)
rating = rating_match.group(1) if rating_match else 'Rating Not Found'

price_match = re.search(r'[ wet](\d+)', text)
price = price_match.group(1) if price_match else 'Price Not Found'

# Writing data to a CSV file
with open('amazon_products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating'])
    writer.writerow([product_name, price, rating])









