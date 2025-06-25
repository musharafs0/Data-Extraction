BOT_NAME = "bayut_scraper"

SPIDER_MODULES = ["bayut_scraper.spiders"]
NEWSPIDER_MODULE = "bayut_scraper.spiders"

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False
FEED_EXPORT_ENCODING = "utf-8"

# Disable Playwright integration if previously added
# DOWNLOAD_HANDLERS = { ... }
# TWISTED_REACTOR = ...


