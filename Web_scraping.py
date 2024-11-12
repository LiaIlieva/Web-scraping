# Required libraries
import time
from bs4 import BeautifulSoup
import requests
import datetime
import csv
import pandas as pd

def createCSVFile():
    # Define the header
    header = ['Title', 'Price', 'Date']

    # Create an empty CSV file with only headers
    with open('AmazonWebScraperData.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)  # Write only the header row

def loopAddInfo():

    # URL of the product page
    URL = 'https://gymbeam.bg/t-shirt-navy-applied-nutrition.html?msclkid=ec42e1db819919cc4faf86e8cc0ab46c&utm_source=bing&utm_medium=cpc&utm_campaign=Shopping%20-%20All%20products&utm_term=4587437398592555&utm_content=NON%20-%20GymBeam#96100'

    # Headers for HTTP request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    # Fetch the page content
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract title and price
    title_element = soup.find(attrs={"data-test": "pdp-product-name"})
    title = title_element.get_text().strip() if title_element else "Title not found"

    price_element = soup.find(attrs={"data-test": "hp-bestsellers-price"})
    price = price_element.get_text().strip()[:-3] if price_element else "Price not found"

    # Save to CSV using a semicolon delimiter
    date = datetime.date.today()
    data = [title, price, date]

    with open('AmazonWebScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=';')  # Use semicolon as the delimiter
        writer.writerow(data)


createCSVFile()

while(True):
    loopAddInfo()
    time.sleep(86400) # checks the data every day