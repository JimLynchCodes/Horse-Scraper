from urllib2 import urlopen
from bs4 import BeautifulSoup as soup
import re

myUrl = 'https://racing.ustrotting.com/waag.aspx'
print (myUrl)

client = urlopen(myUrl)
page_html = client.read()
client.close()

print(page_html);

page_soup = soup(page_html, "html.parser")
# print(page_soup)

# css_soup

race_card_links = page_soup.select("a")
print(race_card_links)

for link in page_soup.select('lnkbtnrace'):
	print links.get_text('Links: ' + link)

	# for links in page_soup.select('a[id*="lnkbtn"]'):