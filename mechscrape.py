import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup as BS
import json

br = Browser()
 
# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)
# Don't add Referer (sic) header
br.set_handle_referer(False)
 
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
 
#Setting the user agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



br.open('https://www.linkedin.com/in/shashankgaurav')


 
#Getting the response in beautifulsoup
soup = BS(br.response().read(), 'lxml')

data={}
positions = soup.find("ul", {"class": "positions"}).find_all('li')
print "My Previous Work Experience : "
for position in positions:
    header = position.header
    tmp={}
    tmp['role']=header.find("h4", {"class": "item-title"}).text
    tmp['organisation-name']=header.find("h5", {"class": "item-subtitle"}).text
    tmp['description']=position.find("p", {"class": "description"}).text
    data['workex']=tmp
    print data['workex'] + "\n"