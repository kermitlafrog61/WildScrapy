from decouple import config


BOT_NAME = "wild"

SPIDER_MODULES = ["wild.spiders"]
NEWSPIDER_MODULE = "wild.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# SPIDER_MIDDLEWARES = {
#     "wild.middlewares.WildSpiderMiddleware": 543,
# }


# DOWNLOADER_MIDDLEWARES = {
#     "wild.middlewares.WildDownloaderMiddleware": 543,
# }

# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

ITEM_PIPELINES = {
   "wild.pipelines.WildPipeline": 100,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


POSTGRES_DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': config('POSTGRES_USER'),
    'password': config('POSTGRES_PASSWORD'),
    'dbname': config('POSTGRES_DB')
}
