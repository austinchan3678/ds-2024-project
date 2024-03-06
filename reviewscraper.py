import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website to fetch its HTML content
url = 'https://www.yelp.com/biz/sizzling-lunch-goleta?osq=Restaurants'
response = requests.get(url)
html_content = response.text

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')


# We want to get the HTML under 
# <span class=" raw__09f24__T4Ezm" lang="en">

# First find all <span> elements with the specified class
target_spans = soup.find_all('span', class_='raw__09f24__T4Ezm')

# Loop through each span element
for span in target_spans:
    # Get the text content of the span
    text_content = span.text.strip()
    
    # Get the value of the lang attribute, if it exists

    # Skips if lang attribute is none, which means it is not a review, or if it is not english language review
    # (Havent tested if it actually filters by language but whatever)
    lang_attribute = span.attrs.get('lang', None)
    if lang_attribute != 'en':
        continue
    
    # Print the text content
    print(text_content)
    print("\n")