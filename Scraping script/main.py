import scraper
import notifications


def main():
    # logs into scraper dummy account
    # scrape_session = scraper.login("br26346", "example")
    # scraper.scrape_catalog(scrape_session)
    notifications.notify_user()




if __name__ == "__main__":
    main()