from mechanize import Browser
from bs4 import BeautifulSoup as BS
import json

br = Browser()
 
# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)
 
# Don't add Referer (sic) header
br.set_handle_referer(False)
 
# Don't handle Refresh redirections
br.set_handle_refresh(False)
 
#Setting the user agent as firefox
br.addheaders = [('User-agent', 'Firefox')]
 
br.open('https://www.linkedin.com/in/shashankgaurav')
 
#Getting the response in beautifulsoup
soup = BS(br.response().read(), 'lxml')

data = {}
data["a"]="b"

print data["a"]

#Fetch Work Experience
i=0
positions = soup.find("ul", {"class": "positions"}).find_all('li')
print "My Previous Work Experience : "
for position in positions:
    header = position.header
    data["workex"][i]=header.find("h4", {"class": "item-title"}).text+ " at " + header.find("h5", {"class": "item-subtitle"}).text
    i+=1

for position in positions:
	print position
	print data[position]
