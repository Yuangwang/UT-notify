import requests
from bs4 import BeautifulSoup


# login info for course schedule
# username: br26346
# password: example


def scrape_catalog():

    # main_page = requests.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/")
    main_page = requests.get("http://www.pythonforbeginners.com")
    c = main_page.content
    soup = BeautifulSoup(c)
    for link in soup.find_all('a'):
        print(link.get("href"))


# logs into course catalog
def login(username, password):

    # base login URL
    login_base = "https://login.utexas.edu/login/cdcservlet?"

    # page to be scraped later
    scraped_page = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/"

    # login URL to directly go to scraping root page
    login_url = login_base + "goto=" + scraped_page + "&ProviderID=" + scraped_page

    # info injected into login page
    login_info = {
        "IDToken1": username,
        "IDToken2": password,

    }

    # remember session to stay logged in
    scrape_session = requests.session()

    # login to registration site on scrape_session, goes to redirect page
    scrape_session.get(login_url)
    login_attempt = scrape_session.post(login_url, data=login_info, headers=dict(referer=login_url))

    # gets form info for redirect, LARES is needed for redirect, no clue what LARES means
    redirect_soup = BeautifulSoup(login_attempt.content, "html.parser")
    lares_value = redirect_soup.find("input", {"name": "LARES"})["value"]
    lares_data = {
        "LARES": lares_value,
    }
    # go through redirect page
    scrape_session.get(login_attempt.url)
    login_done = scrape_session.post(login_attempt.url, data=lares_data, headers=dict(referer=login_url))

    test = scrape_session.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/")
    print(test.text)
