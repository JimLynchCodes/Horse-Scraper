from urllib2 import urlopen
from bs4 import BeautifulSoup as soup
import re

myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
print (myUrl)

client = urlopen(myUrl)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
# print(page_html)

# css_soup

# race_card_links = page_soup.select("a", {"id":".*_lnkbtn"})
# race_card_links = page_soup.find_all(re.compile("_lnkbtnrace_"));
# print(race_card_links)

for links in page_soup.select('a'):
# for links in page_soup.select('a[id*="lnkbtn"]'):
    print links.get_text()