import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.youtube.com')
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

for h1 in soup.find_all('h2'):
    print(h1.text)