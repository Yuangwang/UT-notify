import requests
import time
import lxml
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
    # injects login info and redirect info to navigate to the base course page

    # for login post form
    login_info = [
        ('IDToken1', username),
        ('IDToken2', password),
        ('login_uri', '/login/cdcservlet'),
        ('login_method', 'GET'),
        ('login_param_MinorVersion', '0'),
        ('login_param_RequestID', '1498963635061'),
        ('login_param_ProviderID', 'https://utdirect.utexas.edu:443/amagent?Realm=/admin/utdirect-realm'),
        ('login_param_MajorVersion', '1'),
        ('IDButton', 'Log In'),
        ('goto', 'https://utdirect.utexas.edu:443/apps/registrar/course_schedule/20179'),
        ('SunQueryParamsString',
         'TWlub3JWZXJzaW9uPTAmUmVxdWVzdElEPTE0OTg5NjM2MzUwNjEmUHJvdmlkZXJJRD1odHRwczovL3V0ZGlyZWN0LnV0ZXhhcy5lZHU6NDQzL2FtYWdlbnQ/UmVhbG09L2FkbWluL3V0ZGlyZWN0LXJlYWxtJklzc3VlSW5zdGFudD0yMDE3LTA3LTAyVDAyOjQ3OjE1WiZNYWpvclZlcnNpb249MQ=='),
        ('encoded', 'false'),
        ('gx_charset', 'UTF-8'),
    ]

    # remember session to stay logged in, store cookies and the such
    scrape_session = requests.session()

    # submit the login info
    scrape_session.post('https://login.utexas.edu/login/UI/Login', data=login_info)
    time.sleep(2)

    # page gets redirected, need to input LARES value to continue, no clue what LARES is
    lares_page = scrape_session.get('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179')
    time.sleep(2)

    # goes through the page and finds the LARES value to input
    lares_soup = BeautifulSoup(lares_page.content, "lxml")
    lares = lares_soup.find('input', {'name': 'LARES'})['value']
    lares_data = [
        ('LARES', lares)
    ]

    # submits the LARES value, this time going into the correct path
    scrape_session.post('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179', data=lares_data)
    time.sleep(2)

    # returns the session for future use
    return scrape_session

