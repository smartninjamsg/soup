from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        url = person_url
        profiles = urlopen(url).read()
        profile_name = BeautifulSoup(profiles)
        profile_detailsclass = profile_name.find("div", {"class": "col-md-8"})
        profile_namelist = profile_detailsclass.find("h1").string
        profile_email = BeautifulSoup(profiles)
        profile_emaillist = profile_email.find("span", attrs={"class": "email"}).string
        #profile_city = profile_detailsclass.find("span", {"data-city"})

        csv_file.write(profile_namelist+ "," +profile_emaillist+"\n")
csv_file.close()





