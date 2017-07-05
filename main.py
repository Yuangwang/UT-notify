import scraper


def main():
    # logs into scraper dummy account
    scrape_session = scraper.login("br26346", "example")
    scraper.scrape_catalog(scrape_session)


if __name__ == "__main__":
    main()