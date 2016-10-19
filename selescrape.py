from bs4 import BeautifulSoup
import os
from pyvirtualdisplay import Display
import selenium
import unicodecsv as csv
from selenium import webdriver

headerList = ['Name', 'Summary', 'Skills', 'Work Experience', 'Projects']

with open('data.csv', 'w') as csvHeaderWriterFile:
	csvHeaderWriter = csv.writer(csvHeaderWriterFile)
	csvHeaderWriter.writerow(headerList)

def parseData(linkedinProfile):
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Chrome('/usr/local/share/chromedriver')

	profile_link=linkedinProfile
	driver.get(profile_link)

	html=driver.page_source
	soup=BeautifulSoup(html, 'lxml')

	with open('data.csv', 'a') as csvWriterFile:
		csvWriter = csv.writer(csvWriterFile)

		# Parse the name of the user
		name = soup.find("h1", {"id": "name"})
		data = []
		data.append(name.text)

		# Parse the summary
		summary = soup.find("section", {"id": "summary"})
		data.append(summary.find("div", {"class": "description"}).text)
		
		# Parse the skills
		skills = soup.find("ul", {"class": "pills"}).find_all('li')
		skillData = ''
		for skill in skills:
			if 'see-less' in skill.get("class"):
				continue
			if 'see-more' in skill.get("class"):
				continue
			skillData = skillData + " " + skill.a.span.text
		data.append(skillData)

		# Parse the Work Experience
		workExperiences = soup.find("ul", {"class": "positions"}).find_all('li')

		workExperienceData = []
		for workExperience in workExperiences:
			header = workExperience.header
			tmp={}
			tmp['role']=header.find("h4", {"class": "item-title"}).text
			tmp['organisation']=header.find("h5", {"class": "item-subtitle"}).text
			tmp['description']=workExperience.find("p", {"class": "description"}).text
			workExperienceData.append(tmp)
		data.append(workExperienceData)

		# Parse the projects.
		projects = soup.find_all("li", {"class": "project"})
		projectData = []
		for project in projects:
			tmp={}
			tmp['title'] = project.header.text
			tmp['description']=project.p.text
			projectData.append(tmp)
		data.append(projectData)
		
		csvWriter.writerow(data)

with open("linkedinProfile.csv", "r") as filestream:
    for line in filestream:
    	line= line[1:-2]
    	print line
        parseData(line)

# parseData("https://www.linkedin.com/in/shashankgaurav")

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
	# print data

	# data["skills"]
	# Fetch the skills of the person.
	# subs = soup.find("ul", {"class": "pills"}).find_all('li')
	# print "Fetching skills"
	# for sub in subs:
	# 	if 'see-less' in sub.get("class"):
	# 		continue
	# 	if 'see-more' in sub.get("class"):
	# 		continue
	# 	print sub.a.span.text


	# Fetch the projects of the person.
	# subs = soup.find_all("li", {"class": "project"})
	# print "Fetching Projects"
	# for sub in subs:
	# 	print sub.header.text
	# 	print sub.p.text




#############################################################

# if(1==2):
# 	display = Display(visible=0, size=(800, 600))
# 	display.start()
# 	driver = webdriver.Chrome('/usr/local/share/chromedriver')

# 	profile_link="https://www.linkedin.com/in/shashankgaurav"
# 	driver.get(profile_link)

# 	html=driver.page_source
# 	soup=BeautifulSoup(html)

# else:
# 	soup=BeautifulSoup(open("profile.html"), 'lxml')


# "data" is the final result array that holds ALL data. 
# data={}

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
# print data

# data["skills"]
# Fetch the skills of the person.
# subs = soup.find("ul", {"class": "pills"}).find_all('li')
# print "Fetching skills"
# for sub in subs:
# 	if 'see-less' in sub.get("class"):
# 		continue
# 	if 'see-more' in sub.get("class"):
# 		continue
# 	print sub.a.span.text


# # Fetch the projects of the person.
# subs = soup.find_all("li", {"class": "project"})
# print "Fetching Projects"
# for sub in subs:
# 	print sub.header.text
# 	print sub.p.text
