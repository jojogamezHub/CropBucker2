import json
import logging
import random
import time
from datetime import date, timedelta

import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver

class Searches:
    def __init__(self, browser):
        self.browser = browser
        self.webdriver = browser.webdriver

    def getGoogleTrends(self, wordsCount):
        searchTerms = []
        i = 0
        while len(searchTerms) < wordsCount:
            i += 1
            r = requests.get(
                f'https://trends.google.com/trends/api/dailytrends?hl={self.browser.localeLang}&ed={(date.today() - timedelta(days=i)).strftime("%Y%m%d")}&geo={self.browser.localeGeo}&ns=15'
            )
            trends = json.loads(r.text[6:])
            for topic in trends["default"]["trendingSearchesDays"][0]["trendingSearches"]:
                searchTerms.append(topic["title"]["query"].lower())
                searchTerms.extend(
                    relatedTopic["query"].lower()
                    for relatedTopic in topic["relatedQueries"]
                )
            searchTerms = list(set(searchTerms))
        del searchTerms[wordsCount : (len(searchTerms) + 1)]
        return searchTerms

    def swagbucksSearches(self, numberOfSearches=400):
        logging.info("[SWAGBUCKS] Starting Swagbucks searches...")

        i = 0
        search_terms = self.getGoogleTrends(numberOfSearches)
        for word in search_terms:
            i += 1
            logging.info("[SWAGBUCKS] " + f"{i}/{numberOfSearches}")
            self.swagbucksSearch(word)
            time.sleep(random.randint(10, 15))

        logging.info("[SWAGBUCKS] Finished Swagbucks searches!")
