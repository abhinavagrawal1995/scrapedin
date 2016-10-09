from bs4 import BeautifulSoup
import os
from pyvirtualdisplay import Display
import selenium
from selenium import webdriver

# make this false while development. It will use the offline profile.html file which is a lot faster.
if(1==2):

	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Chrome('/usr/local/share/chromedriver')

	profile_link="https://www.linkedin.com/in/shashankgaurav"
	driver.get(profile_link)

	html=driver.page_source
	soup=BeautifulSoup(html)

else:
	soup=BeautifulSoup(open("profile.html"))

# "data" is the final result array that holds ALL data. 
data={}

#commented sections work properly. commented out to reduce time to run.

# data["summary"]
# sub = soup.find("section", {"id": "summary"})
# print "Fetching summary"
# tmp={}
# tmp['description']=sub.find("div", {"class": "description"}).text
# data['description']=tmp
# print data['description'] 
# print "\n"


# data["workex"]
# subs = soup.find("ul", {"class": "positions"}).find_all('li')
# print "Fetching workex"
# for sub in subs:
#     header = sub.header
#     tmp={}
#     tmp['role']=header.find("h4", {"class": "item-title"}).text
#     tmp['organisation-name']=header.find("h5", {"class": "item-subtitle"}).text
#     tmp['description']=sub.find("p", {"class": "description"}).text
#     data['workex']=tmp
#     print data['workex'] 
#     print "\n"

# data["skills"]
# works till the skills that are viewd before the "see more" part. gives error on "see more" item.
subs = soup.find("ul", {"class": "pills"}).find_all('li')
print "Fetching skills"
for sub in subs:
	if sub.find(class_='skill see-less'):
		continue
	if sub.find(class_='skill see-more'):
		continue
	print sub
	tmp={}
	print sub.find("span", {"class": "wrap"}).text

