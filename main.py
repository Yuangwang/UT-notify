import scraper
import requests

def main():
    # logs into scraper dummy account
    scrape_session = scraper.login("br26346", "29900770ben")
    cookies = {
        'sunIdentityServerAuthNServer-prod': 'https%3A%2F%2Futlogin-core.its.utexas.edu%3A443',
        'SC': 'AQEBBwID6gIQOTczQUI1MEVDQzNFMzk1QwYkVk5mMXk2WG1jL0tyQVg3VWpPcEFkSUtOdHNNcWphc2liK3dJBAoxNDk4ODk5OTU1BQw3MC4xMjMuMzQuODQDBnl3ODY3NQoBWQiAl/G9SrhriB13pVV6tUjzOpd8WqbGiSrAwP+v0jjfmHYOfPuNflfp7/y5/IiPz9sUewFEDRugw7msBsRglNOwlhUUuPzwzVqdUI0S2pCEnAiYPSpHLTVoiTW8HWf5vG8yPv5JjLfPKf1178JRZaySH68Uc7Zqi74R9lY/LfAtZyo=',
        'utlogin-prod': 'AQIC5wM2LY4Sfcw91Gi89wXtdG5SRrH-3MeM3BgmhJkUvAQ.*AAJTSQACMDIAAlMxAAIwNQACU0sAEzQ4OTA3NTEyNzIxNzQwMzUyOTI.*',
        'NSC_vue-qspe_443': 'ffffffffc3a018e645525d5f4f58455e445a4a42378b',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/',
        'Connection': 'keep-alive',
    }

    params = (
        ('ccyys', '20179'),
        ('search_type_main', 'FIELD'),
        ('fos_fl', 'E E'),
        ('level', 'L'),
        ('x', '79'),
        ('y', '20'),
    )
    test = scrape_session.get('https://utdirect.utexas.edu/apps/registrar/course_schedule/20179/results/', headers=headers, params=params, cookies=cookies)
    print(test.text)

if __name__ == "__main__":
    main()