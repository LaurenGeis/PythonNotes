import request, bs4, lxml
from pip._vendor import requests

res = requests.get('https://nostarch.com')
# request.get() used to download the main page from the URL
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, 'html.parser')
# passes text attributes of the response to bs4.BeautifulSoup
type(no_starch_soup)

# you can pass a HTML file into bs4.BeautifulSoup(exampleFile, 'html.parser)
# lxml may work faster to parse. Installed this and added to import



