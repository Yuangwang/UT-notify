import requests
import time
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
    #TODO fix redudencies in code, especially cookies/scrape_session
    # a lot of stuff to inject into page to mimic browser
    # info injected into login page
    login_cookies = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'AMAuthCookie-prod': 'AQIC5wM2LY4SfczfAysxqt0fcPnXQij-oosOZX5P8m7vitw.*AAJTSQACMDIAAlNLABQtMjQ3NjI5MTczNTcxNzc1NTgyOQACUzEAAjA3*',
        'amlbcookie': '3878225554.47873.0000',
    }
    login_headers = {
        'Origin': 'https://login.utexas.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892703839&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A03Z',
        'Connection': 'keep-alive',
    }
    login_info = {
        "IDToken1": username,
        "IDToken2": password,
        "login_uri": "/login/cdcservlet",
        "login_method": "GET",
        "login_param_MinorVersion": "0",
        "login_param_RequestID": "1498892703839",
        "login_param_ProviderID": "https://utdirect.utexas.edu:443/amagent?Realm=/admin/utdirect-realm",
        "login_param_IssueInstant": "2017-07-01T07:05:03Z",
        "login_param_MajorVersion": "1",
        "IDButton": "Log In",
        "goto": "https://utdirect.utexas.edu:443/apps/registrar/course_schedule/20179",
        "SunQueryParamsString": "TWlub3JWZXJzaW9uPTAmUmVxdWVzdElEPTE0OTg4OTI3MDM4MzkmUHJvdmlkZXJJRD1odHRwczovL3V0ZGlyZWN0LnV0ZXhhcy5lZHU6NDQzL2FtYWdlbnQ/UmVhbG09L2FkbWluL3V0ZGlyZWN0LXJlYWxtJklzc3VlSW5zdGFudD0yMDE3LTA3LTAxVDA3OjA1OjAzWiZNYWpvclZlcnNpb249MQ==",
        "encoded": "false",
        "gx_charset": "UTF-8"

    }

    # inject info into next page
    cookies_20179_redir = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'NSC_vue-qspe_443': 'ffffffffc3a018e545525d5f4f58455e445a4a42378b',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
    }
    headers_20179_redir= {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892703839&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A03Z',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }

    # and again
    cookies_cdc = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'amlbcookie': '3878225554.47873.0000',
        'utlogin-prod': 'AQIC5wM2LY4SfcyZUS06UlbiYHE6KDqwPkPTdMhwfYHo4MM.*AAJTSQACMDIAAlNLABQtNDAxMjUyNTAwMjQxMDM5MDQ2MAACUzEAAjA3*',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
    }
    headers_cdc = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892703839&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A03Z',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    params_cdc = (
        ('goto', 'https://utdirect.utexas.edu:443/apps/registrar/course_schedule/20179'),
        ('RequestID', '1498892717205'),
        ('MajorVersion', '1'),
        ('MinorVersion', '0'),
        ('ProviderID', 'https://utdirect.utexas.edu:443/amagent?Realm=/admin/utdirect-realm'),
        ('IssueInstant', '2017-07-01T07:05:17Z'),
    )

    # and again.
    cookies_favi = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'amlbcookie': '3878225554.47873.0000',
        'utlogin-prod': 'AQIC5wM2LY4SfcyZUS06UlbiYHE6KDqwPkPTdMhwfYHo4MM.*AAJTSQACMDIAAlNLABQtNDAxMjUyNTAwMjQxMDM5MDQ2MAACUzEAAjA3*',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
    }
    headers_favi = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892717205&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A17Z',
        'Connection': 'keep-alive',
    }

    # and again..

    cookies_20179_post = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
        'NSC_vue-qspe_443': 'ffffffffc3a018e545525d5f4f58455e445a4a42378b',
    }
    headers_20179_post = {
        'Origin': 'https://login.utexas.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892717205&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A17Z',
        'Connection': 'keep-alive',
    }
    data_20179_post = [
        ('LARES',
         'PGxpYjpBdXRoblJlc3BvbnNlIHhtbG5zOmxpYj0iaHR0cDovL3Byb2plY3RsaWJlcnR5Lm9yZy9zY2hlbWFzL2NvcmUvMjAwMi8xMiIgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6MS4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDpwcm90b2NvbCIgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIFJlc3BvbnNlSUQ9InMwOTc2ZDA2MWE3ZWVmZjdkYzI1N2RkNWE4MjYwODAzMTQ0NmQ4MzljIiAgSW5SZXNwb25zZVRvPSIxNDk4ODkyNzE3MjA1IiBNYWpvclZlcnNpb249IjEiIE1pbm9yVmVyc2lvbj0iMCIgSXNzdWVJbnN0YW50PSIyMDE3LTA3LTAxVDA3OjA1OjE3WiI+PHNhbWxwOlN0YXR1cz4KPHNhbWxwOlN0YXR1c0NvZGUgVmFsdWU9InNhbWxwOlN1Y2Nlc3MiPgo8L3NhbWxwOlN0YXR1c0NvZGU+Cjwvc2FtbHA6U3RhdHVzPgo8c2FtbDpBc3NlcnRpb24gIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiICB4bWxuczpsaWI9Imh0dHA6Ly9wcm9qZWN0bGliZXJ0eS5vcmcvc2NoZW1hcy9jb3JlLzIwMDIvMTIiICBpZD0iczkyNTdjMWM3NWFiY2NkMzhmMDBiZWUyMWM4NTVmMDYxOWVhNDdkNzYwNyIgTWFqb3JWZXJzaW9uPSIxIiBNaW5vclZlcnNpb249IjAiIEFzc2VydGlvbklEPSJzOTI1N2MxYzc1YWJjY2QzOGYwMGJlZTIxYzg1NWYwNjE5ZWE0N2Q3NjA3IiBJc3N1ZXI9Imh0dHBzOi8vdXRsYy1wMDQuaXRzLnV0ZXhhcy5lZHU6NDQzL29wZW5hbS9jZGNzZXJ2bGV0IiBJc3N1ZUluc3RhbnQ9IjIwMTctMDctMDFUMDc6MDU6MTdaIiBJblJlc3BvbnNlVG89IjE0OTg4OTI3MTcyMDUiIHhzaTp0eXBlPSJsaWI6QXNzZXJ0aW9uVHlwZSI+CjxzYW1sOkNvbmRpdGlvbnMgIE5vdEJlZm9yZT0iMjAxNy0wNy0wMVQwNzowNToxN1oiIE5vdE9uT3JBZnRlcj0iMjAxNy0wNy0wMVQwNzowNjoxN1oiID4KPHNhbWw6QXVkaWVuY2VSZXN0cmljdGlvbkNvbmRpdGlvbj4KPHNhbWw6QXVkaWVuY2U+aHR0cHM6Ly91dGRpcmVjdC51dGV4YXMuZWR1OjQ0My9hbWFnZW50P1JlYWxtPS9hZG1pbi91dGRpcmVjdC1yZWFsbTwvc2FtbDpBdWRpZW5jZT4KPC9zYW1sOkF1ZGllbmNlUmVzdHJpY3Rpb25Db25kaXRpb24+Cjwvc2FtbDpDb25kaXRpb25zPgo8c2FtbDpBdXRoZW50aWNhdGlvblN0YXRlbWVudCAgQXV0aGVudGljYXRpb25NZXRob2Q9IlVUTG9naW5Mb2NrQW5kRlBTIiBBdXRoZW50aWNhdGlvbkluc3RhbnQ9IjIwMTctMDctMDFUMDc6MDU6MTdaIiBSZWF1dGhlbnRpY2F0ZU9uT3JBZnRlcj0iMjAxNy0wNy0wMVQwNzowNjoxN1oiIHhzaTp0eXBlPSJsaWI6QXV0aGVudGljYXRpb25TdGF0ZW1lbnRUeXBlIj48c2FtbDpTdWJqZWN0ICAgeHNpOnR5cGU9ImxpYjpTdWJqZWN0VHlwZSI+PHNhbWw6TmFtZUlkZW50aWZpZXIgTmFtZVF1YWxpZmllcj0iaHR0cHM6Ly91dGxjLXAwNC5pdHMudXRleGFzLmVkdTo0NDMvb3BlbmFtL2NkY3NlcnZsZXQiPkFRSUM1d00yTFk0U2Zjd1BRNFVaMmlaSmNLQnVfWmRCUWRyNF9FRmJfNWpud1ZrLipBQUpUU1FBQ01ESUFBbE14QUFJd053QUNVMHNBRkMwME1ERXlOVEkxTURBeU5ERXdNemt3TkRZdyo8L3NhbWw6TmFtZUlkZW50aWZpZXI+CjxzYW1sOlN1YmplY3RDb25maXJtYXRpb24+CjxzYW1sOkNvbmZpcm1hdGlvbk1ldGhvZD51cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjA6Y206YmVhcmVyPC9zYW1sOkNvbmZpcm1hdGlvbk1ldGhvZD4KPC9zYW1sOlN1YmplY3RDb25maXJtYXRpb24+CjxsaWI6SURQUHJvdmlkZWROYW1lSWRlbnRpZmllciAgTmFtZVF1YWxpZmllcj0iaHR0cHM6Ly91dGxjLXAwNC5pdHMudXRleGFzLmVkdTo0NDMvb3BlbmFtL2NkY3NlcnZsZXQiID5BUUlDNXdNMkxZNFNmY3dQUTRVWjJpWkpjS0J1X1pkQlFkcjRfRUZiXzVqbndWay4qQUFKVFNRQUNNRElBQWxNeEFBSXdOd0FDVTBzQUZDMDBNREV5TlRJMU1EQXlOREV3TXprd05EWXcqPC9saWI6SURQUHJvdmlkZWROYW1lSWRlbnRpZmllcj4KPC9zYW1sOlN1YmplY3Q+PHNhbWw6U3ViamVjdExvY2FsaXR5ICBJUEFkZHJlc3M9IjE0Ni42LjQxLjIzMSIgRE5TQWRkcmVzcz0idXRsYy1wMDQuaXRzLnV0ZXhhcy5lZHUiIC8+PGxpYjpBdXRobkNvbnRleHQ+PGxpYjpBdXRobkNvbnRleHRDbGFzc1JlZj5odHRwOi8vd3d3LnByb2plY3RsaWJlcnR5Lm9yZy9zY2hlbWFzL2F1dGhjdHgvY2xhc3Nlcy9QYXNzd29yZDwvbGliOkF1dGhuQ29udGV4dENsYXNzUmVmPjxsaWI6QXV0aG5Db250ZXh0U3RhdGVtZW50UmVmPmh0dHA6Ly93d3cucHJvamVjdGxpYmVydHkub3JnL3NjaGVtYXMvYXV0aGN0eC9jbGFzc2VzL1Bhc3N3b3JkPC9saWI6QXV0aG5Db250ZXh0U3RhdGVtZW50UmVmPjwvbGliOkF1dGhuQ29udGV4dD48L3NhbWw6QXV0aGVudGljYXRpb25TdGF0ZW1lbnQ+PC9zYW1sOkFzc2VydGlvbj4KPGxpYjpQcm92aWRlcklEPmh0dHBzOi8vdXRsYy1wMDQuaXRzLnV0ZXhhcy5lZHU6NDQzL29wZW5hbS9jZGNzZXJ2bGV0PC9saWI6UHJvdmlkZXJJRD48L2xpYjpBdXRoblJlc3BvbnNlPgo='),
    ]

    # and again...
    cookies_login_get = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'amlbcookie': '3878225554.47873.0000',
        'utlogin-prod': 'AQIC5wM2LY4SfcyZUS06UlbiYHE6KDqwPkPTdMhwfYHo4MM.*AAJTSQACMDIAAlNLABQtNDAxMjUyNTAwMjQxMDM5MDQ2MAACUzEAAjA3*',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
    }
    headers_login_get = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892717205&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A17Z',
        'Connection': 'keep-alive',
    }

    # ang again....
    cookies_openam = {
        'JSESSIONID': '892C36810A2F0CFE5EDF9187FCF04C98',
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'amlbcookie': '3878225554.47873.0000',
        'utlogin-prod': 'AQIC5wM2LY4SfcyZUS06UlbiYHE6KDqwPkPTdMhwfYHo4MM.*AAJTSQACMDIAAlNLABQtNDAxMjUyNTAwMjQxMDM5MDQ2MAACUzEAAjA3*',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
    }
    headers_openam = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://login.utexas.edu/login/cdcservlet?goto=https%3A%2F%2Futdirect.utexas.edu%3A443%2Fapps%2Fregistrar%2Fcourse_schedule%2F20179&RequestID=1498892717205&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Futdirect.utexas.edu%3A443%2Famagent%3FRealm%3D%2Fadmin%2Futdirect-realm&IssueInstant=2017-07-01T07%3A05%3A17Z',
        'Connection': 'keep-alive',
    }

    #and again.....
    cookies_20179_moved = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
        'utlogin-prod': 'AQIC5wM2LY4SfcwPQ4UZ2iZJcKBu_ZdBQdr4_EFb_5jnwVk.*AAJTSQACMDIAAlMxAAIwNwACU0sAFC00MDEyNTI1MDAyNDEwMzkwNDYw*',
        'NSC_vue-qspe_443': 'ffffffffc3a018e545525d5f4f58455e445a4a42378b',
    }
    headers_20179_moved = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20179',
        'Connection': 'keep-alive',
    }

    # finally done
    cookies_finished = {
        '__cfduid': 'd394fc3dc36811d46d7c7c831e36203671498892074',
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
        'utlogin-prod': 'AQIC5wM2LY4SfcwPQ4UZ2iZJcKBu_ZdBQdr4_EFb_5jnwVk.*AAJTSQACMDIAAlMxAAIwNwACU0sAFC00MDEyNTI1MDAyNDEwMzkwNDYw*',
        'SC': 'AQEBBwID6gIQODMyRENDRDNDQzUwQUE1NQYkNmxzeDUxdzN3Q2VjMmdNM0NkZE5XYmV2MjduSUhZZ1Y2QjhpBAoxNDk4ODk2MzE3BQw3MC4xMjMuMzQuODQDB2JyMjYzNDYKAVkIgG/njamX0NsDbBgojcnKnmSqTdtYanbKb+WB8Ga1XQcHsqXba83kUk+6mztmgzyM8/PtNgkwZtDT0iE+Rr4+S7WqBtx3REmEjUuPSN5cc+/dI/0rlshXimTnY3o2N2152MDkm8mPgh3ubXuvj5M3qH6FtAw62d2jsocl+DXgfGXo',
        'NSC_vue-qspe_443': 'ffffffffc3a018e545525d5f4f58455e445a4a42378b',
    }

    headers_finished = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20179',
        'Connection': 'keep-alive',
    }
    # remember session to stay logged in
    scrape_session = requests.session()

    # login to registration site on scrape_session, redirects several times and eventaully ends up at the course page
    scrape_session.post("https://login.utexas.edu/login/UI/Login", data=login_info, headers=login_headers, cookies=login_cookies)
    time.sleep(1)
    scrape_session.get('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179', headers=headers_20179_redir,
                       cookies=cookies_20179_redir)
    time.sleep(1)
    scrape_session.get('https://login.utexas.edu/login/cdcservlet', headers=headers_cdc, params=params_cdc,
                       cookies=cookies_cdc)
    time.sleep(1)
    scrape_session.get('https://login.utexas.edu/favicon.ico', headers=headers_favi, cookies=cookies_favi)
    time.sleep(1)
    scrape_session.post('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179', headers=headers_20179_post,
                        cookies=cookies_20179_post,data=data_20179_post)
    time.sleep(1)
    scrape_session.get('https://login.utexas.edu/login', headers=headers_login_get, cookies=cookies_login_get)
    time.sleep(1)
    scrape_session.get('https://login.utexas.edu/openam/', headers=headers_openam, cookies=cookies_openam)
    time.sleep(1)
    scrape_session.get('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179', headers=headers_20179_moved,
                       cookies=cookies_20179_moved)
    time.sleep(1)
    scrape_session.get('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/', headers=headers_finished,
                       cookies=cookies_finished)
    return scrape_session
