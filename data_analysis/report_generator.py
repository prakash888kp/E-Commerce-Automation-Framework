import pandas as pd

# Load data from both sources
selenium_data = pd.read_csv('/Users/prakashk/Documents/Python-Assesment/selenium_automation/data/amazon_products.csv')
appium_data = pd.read_csv('/Users/prakashk/Documents/Python-Assesment/ocr_processing/amazon_products.csv')

# Rename columns to align names for comparison
appium_data = appium_data.rename(columns={'Name': 'Product Name', 'Price': 'Appium Price', 'Rating': 'Appium Rating'})

# Merge both datasets on 'Product Name'
merged_data = pd.merge(selenium_data, appium_data, on='Product Name', how='outer')

# List items with matching prices
matching_prices = merged_data[merged_data['Price'] == merged_data['Appium Price']]

# Items with discrepancies
price_discrepancies = merged_data[merged_data['Price'] != merged_data['Appium Price']]

# Final summary report
summary_report = {
    'Matching Prices Count': len(matching_prices),
    'Discrepancies Count': len(price_discrepancies)
}

# Output the results
print("Items with Matching Prices:")
print(matching_prices)

print("\nItems with Price Discrepancies:")
print(price_discrepancies)

print("\nSummary Report:")
print(summary_report)
