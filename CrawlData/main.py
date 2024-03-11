import crawl_data as cd

def main():
    crawl = cd.CrawlData()
    crawl.devideDataTypes(cd.RAW_URL_FILENAME)
    crawl.crawlDataNormal()
    crawl.crawlDataHaveSubtitle()

if __name__ == "__main__":
    main()