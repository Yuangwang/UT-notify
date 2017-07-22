import scraper
import notifications
import os


def main():
    # logs into scraper dummy account
    scrape_session = scraper.login(os.environ.get("scrape_user"), os.environ.get("scrape_pass"))
    scraper.scrape_catalog(scrape_session)
    notifications.notify_user()




if __name__ == "__main__":
    main()