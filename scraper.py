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
        "login_uri": "/login/UI/Login",
        "login_method": "GET",
        "IDButton": "Log In",
        "encoded": "false",
        "gx_charset": "UTF-8"
    }

    # remember session to stay logged in
    scrape_session = requests.session()

    # login to registration site on scrape_session
    scrape_session.get(login_url)
    login_attempt = scrape_session.post(login_url, data=login_info, headers=dict(referer=login_url))

    # TODO fix redirect, right now redirects to another POST form that has a submission
    print(login_attempt.text)
