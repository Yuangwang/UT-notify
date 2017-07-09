import scraper
import psycopg2


def main():
    # logs into scraper dummy account
    scrape_session = scraper.login("br26346", "29900770ben")
    scraper.scrape_catalog(scrape_session)


    print(unique_in_db)


if __name__ == "__main__":
    main()