import requests
from bs4 import BeautifulSoup

# Target URL (You can replace this with any public news website)
URL = 'https://indianexpress.com/'

# Step 1: Fetch HTML
response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f"Failed to fetch page: {response.status_code}")

html_content = response.text

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract headlines from <h2> and <title> tags
headlines = []

# Get the main title of the page
page_title = soup.title.string.strip() if soup.title else 'No title found'
headlines.append(f"PAGE TITLE: {page_title}")

# Find all <h2> elements
h2_tags = soup.find_all('h2')
for tag in h2_tags:
    text = tag.get_text(strip=True)
    if text:  # Avoid empty strings
        headlines.append(text)

# Step 4: Save headlines to .txt file
output_file = 'headlines.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for headline in headlines:
        f.write(headline + '\n')

print(f"{len(headlines)} headlines saved to {output_file}")
