Project Structure
The project is organized into various folders:

- **selenium_automation**: Contains Selenium scripts to scrape e-commerce data.
- **appium_automation**: Hosts Appium scripts to perform mobile interactions.
- **ocr_processing**: Includes scripts to process images using OCR.
- **data_analysis**: Employs data comparison and reporting scripts.

### Execution Flow
The execution sequence for this project is as follows:

1. **Selenium Automation**:
    - Runs the `main.py` script in the `selenium_automation` folder to scrape data from e-commerce websites.
2. **Appium Automation**:
    - Executes `main.py` in the `appium_automation` folder to perform mobile app interactions.
3. **OCR Processing**:
    - Uses `main.py` in the `ocr_processing` folder to extract text from captured screenshots.
4. **Data Analysis**:
    - Runs `report_generator.py` in the `data_analysis` folder to compare and generate reports.

### Test Description
1. **Selenium Web Automation**:
    - Utilizes Selenium to scrape data from e-commerce platforms.
2. **Appium Mobile Automation**:
    - Interacts with a mobile app and captures screenshots.
3. **OCR Image Processing**:
    - Extracts text from the captured screenshots using an OCR library.
4. **Data Analysis and Reporting**:
    - Generates reports and compares OCR-extracted data with the Selenium-scraped data.

### Deliverables
- Python script (.py file) containing the automation, OCR processing, and data comparison logic.
- `requirements.txt` file with all necessary Python libraries.
- `README.md` file explaining the setup and execution process.

## Setup and Execution
Please ensure you've installed the required libraries from `requirements.txt` using `pip install -r requirements.txt`. Then follow these steps:

1. Navigate to the respective directories (e.g., `selenium_automation`, `appium_automation`, etc.).
2. Run the main scripts .py files in each directory to execute the specific task.
