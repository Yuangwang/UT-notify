import requests
import time
import data
import psycopg2
import os
from bs4 import BeautifulSoup

'''All functions in this file contribute to the scraping of data to insert into my own database'''


# fun fact UT has 402 pages in their course directory

# scrapes the entire ut catalog
def scrape_catalog(session):
    # opens connection and cursor for future use
    db_name = os.environ.get("db_name")
    user = os.environ.get("db_user")
    host = os.environ.get("db_host")
    password = os.environ.get("db_password")
    con = psycopg2.connect("dbname=%s user=%s host=%s password=%s" % (db_name,user,host,password))

    cur = con.cursor()

    # store current database values in a set for later reference to see if values have changed
    db_set = data.current_unique_data(cur)

    # used later to check for which unique numebers to delete
    online_uniques = []

    # root page to be scraped
    next_page = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20189/results/?ccyys=20199&" \
                "search_type_main=UNIQUE&unique_number=&start_unique=00000&end_unique=99999"

    # tests to see if the end has been reached, if not keeps scraping
    while next_page is not None:
        next_page = scrape_page(session, next_page, db_set, online_uniques, cur, con)
        time.sleep(1)

    # convert into set for easier compare
    online_set = set(online_uniques)

    # deletes extra courses that no longer exist
    data.delete_extra(db_set, online_set, cur, con)

    # close connections and cursor
    cur.close()
    con.close()


# searches a single page for the class data, returns the next page to be searched, returns None if last page
# also adds to the growing list of uniques numbers that the scraper has found through on_uniques
def scrape_page(session, page, db_uniques, on_uniques, cur, con):
    # full catalog in main_page
    main_page = session.get(page)
    page_soup = BeautifulSoup(main_page.content, "lxml")

    # go through each row of the catalog
    for row in page_soup.find_all("tr"):

        # unique check only allows the class to be stored once its data is compeltely scraped
        unique_check = False

        for col in row.find_all("td"):
            # finds the class name for following courses
            try:
                if col["class"][0] == "course_header":
                    name = col.get_text()

            # finds and stores the rest of the course info
            except KeyError:
                try:
                    if col["data-th"] == "Unique":
                        unique = int(col.get_text())
                        unique_check = True
                        on_uniques.append(unique)
                    if col["data-th"] == "Days":
                        day = col.get_text()
                    if col["data-th"] == "Hour":
                        hour = col.get_text()
                    if col["data-th"] == "Room":
                        room = col.get_text()
                    if col["data-th"] == "Instructor":
                        professor = col.get_text()
                    if col["data-th"] == "Status":
                        status = col.get_text()
                except KeyError:
                    continue

        # called when a single class has all of its info and stores its info
        if unique_check is True:
            course = CourseInfo(unique, day, hour, room, professor, status, name)
            course.store(db_uniques, cur, con)

    # look for the next page to crawl
    try:
        test = page_soup.find("a", {"id": "next_nav_link"})["href"]
        return "https://utdirect.utexas.edu/apps/registrar/course_schedule/20199/results/" + test
    except TypeError:
        return None


# contains the info for the course
class CourseInfo:
    def __init__(self, unique_num, day, hour, room, professor, status, name):
        self.unique_num = unique_num
        self.day = day
        self.hour = hour
        self.room = room
        self.professor = professor
        self.status = status
        self.name = name

    # stores data into SQL database
    def store(self, db_uniques, cur, con):
        # update the existing class, class already exists
        if self.unique_num in db_uniques:
            data.update_class(self, cur, con)

        # insert class, class doesn't exist yet
        else:
            data.insert_class(self, cur, con)
        return


# logs into course catalog
# takes in the log in info for the scraper account
# returns the session that is already logged in
def login(username, password):
    # for login post form
    login_info = [
        ("IDToken1", username),
        ("IDToken2", password),
        ("login_uri", "/login/cdcservlet"),
        ("login_method", "GET"),
        ("IDButton", "Log In"),
        ("goto", "https://utdirect.utexas.edu:443/apps/registrar/course_schedule/20199"),
        ("encoded", "false"),
        ("gx_charset", "UTF-8"),
    ]

    # remember session to stay logged in, store cookies and the such
    scrape_session = requests.session()

    # submit the login info
    scrape_session.post("https://login.utexas.edu/login/UI/Login", data=login_info)
    time.sleep(1)

    # page gets redirected, need to input LARES value to continue, no clue what LARES is
    lares_page = scrape_session.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20199")
    time.sleep(1)

    # goes through the page and finds the LARES value to input
    lares_soup = BeautifulSoup(lares_page.content, "lxml")
    lares = lares_soup.find("input", {"name": "LARES"})["value"]
    lares_data = [
        ("LARES", lares)
    ]

    # submits the LARES value, this time going into the correct path
    scrape_session.post("https://utdirect.utexas.edu/apps/registrar/course_schedule/20199", data=lares_data)
    time.sleep(1)

    # returns the session for future use
    return scrape_session
