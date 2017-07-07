import requests
import time
from bs4 import BeautifulSoup


# login info for course schedule
# username: br26346
# password: example

# fun fact UT has 402 pages in their course directory

# scrapes the entire ut catalog
def scrape_catalog(session):

    # root page to be scraped
    next_page = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/results/?ccyys=20179&" \
                 "search_type_main=UNIQUE&unique_number=&start_unique=00000&end_unique=99999"

    # tests to see if the end has been reached, if not keeps scraping
    while next_page is not None:
        next_page = scrape_page(session, next_page)
        time.sleep(1)


# searches a single page for the class data, returns the next page to be searched, returns None if last page
def scrape_page(session, page):
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
                        unique = col.get_text()
                        unique_check = True
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
            print(unique+day+hour+room+professor+status+name)

    # look for the next page to crawl
    try:
        test = page_soup.find("a", {"id": "next_nav_link"})["href"]
        return "https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/results/" + test
    except TypeError:
        return None


# contains the info for the course
class CourseInfo:
    def __init__(self, unique, day, hour, room, professor, status, name):
        self.unique = unique
        self.day = day
        self.hour = hour
        self.room = room
        self.professor = professor
        self.status = status
        self.name = name

    # stores data into SQL database
    def store(self):
        # TODO finish this method to store CourseInfo into a SQL database
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
        ("login_param_MinorVersion", "0"),
        ("login_param_RequestID", "1498963635061"),
        ("login_param_ProviderID", "https://utdirect.utexas.edu:443/amagent?Realm=/admin/utdirect-realm"),
        ("login_param_MajorVersion", "1"),
        ("IDButton", "Log In"),
        ("goto", "https://utdirect.utexas.edu:443/apps/registrar/course_schedule/20179"),
        ("SunQueryParamsString",
         "TWlub3JWZXJzaW9uPTAmUmVxdWVzdElEPTE0OTg5NjM2MzUwNjEmUHJvdmlkZXJJRD1odHRwczovL3V0ZGlyZWN0L"
         "nV0ZXhhcy5lZHU6NDQzL2FtYWdlbnQ/UmVhbG09L2FkbWluL3V0ZGlyZWN0LXJlYWxtJklzc3VlSW5zdGFudD0yMD"
         "E3LTA3LTAyVDAyOjQ3OjE1WiZNYWpvclZlcnNpb249MQ=="),
        ("encoded", "false"),
        ("gx_charset", "UTF-8"),
    ]

    # remember session to stay logged in, store cookies and the such
    scrape_session = requests.session()

    # submit the login info
    scrape_session.post("https://login.utexas.edu/login/UI/Login", data=login_info)
    time.sleep(1)

    # page gets redirected, need to input LARES value to continue, no clue what LARES is
    lares_page = scrape_session.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179")
    time.sleep(1)

    # goes through the page and finds the LARES value to input
    lares_soup = BeautifulSoup(lares_page.content, "lxml")
    lares = lares_soup.find("input", {"name": "LARES"})["value"]
    lares_data = [
        ("LARES", lares)
    ]

    # submits the LARES value, this time going into the correct path
    scrape_session.post("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179", data=lares_data)
    time.sleep(1)

    # returns the session for future use
    return scrape_session
