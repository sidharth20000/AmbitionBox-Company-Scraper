from bs4 import BeautifulSoup as bs
import requests
import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")
db1 = db["Ambition_Box"]
coll = db1["Companies_Information"]

COMPANY_NAME = []
RATING = []
REVIEWS = []
DOMAIN = []
LOCATION = []
DURATION = []
EMPLOYEES = []

for page_no in range(1, 334):
    URL = f"https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={page_no}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) '
                      'Chrome/80.0.3987.162 Safari/537.36'
    }
    webpage = requests.get(URL, headers=headers).text
    scrap = bs(webpage, "html.parser")
    name_class = scrap.find_all("h2", class_="company-name bold-title-l")
    rating_class = scrap.find_all("div", class_="rating-wrapper")
    location_class = scrap.find_all("div", class_="company-basic-info")
    for n, r, l in zip(name_class, rating_class, location_class):
        try:
            if len(l.find_all("p")) == 4:
                DOMAIN.append(l.find_all("p")[0].text.strip())
                LOCATION.append(l.find_all("p")[1].text.strip())
                DURATION.append(l.find_all("p")[2].text.strip())
                EMPLOYEES.append(l.find_all("p")[3].text.strip())

                COMPANY_NAME.append(n.get("title"))
                RATING.append(r.find("p").text.strip())
                REVIEWS.append(r.find("a").text.strip())

        except:
            continue

info = {
    "Name": COMPANY_NAME,
    "Rating": RATING,
    "Reviews": REVIEWS,
    "Domain": DOMAIN,
    "Location": LOCATION,
    "Duration": DURATION,
    "No. of Employees": EMPLOYEES
}

coll.insert_one(info)

