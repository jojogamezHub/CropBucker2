from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwagbucksBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()  # Make sure to use the appropriate webdriver for your browser

    def login(self):
        self.driver.get("https://www.swagbucks.com/")
        
        # Find and click the login button
        login_button = self.driver.find_element(By.CLASS_NAME, "login")
        login_button.click()

        # Enter username and password
        username_input = self.driver.find_element(By.ID, "sbxJxMMd")
        password_input = self.driver.find_element(By.ID, "sbxJxMMd")  # Replace with the actual ID of the password input field
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # Submit the form
        login_form = self.driver.find_element(By.ID, "login-form")  # Replace with the actual ID of the login form
        login_form.submit()

    def perform_searches(self, search_terms):
        for term in search_terms:
            self.swagbucks_search(term)
            time.sleep(random.randint(10, 15))

    def swagbucks_search(self, term):
        logging.info("[SWAGBUCKS] Starting Swagbucks searches...")

        i = 0
        search_terms = self.getGoogleTrends(numberOfSearches)
        for word in search_terms:
            i += 1
            logging.info("[SWAGBUCKS] " + f"{i}/{numberOfSearches}")
            self.swagbucksSearch(word)
            time.sleep(random.randint(10, 15))

        logging.info("[SWAGBUCKS] Finished Swagbucks searches!")
        pass

    def close(self):
        self.driver.quit()

# Example usage:
username = "your_username"
password = "your_password"
swagbucks_bot = SwagbucksBot(username, password)
swagbucks_bot.login()

# Get search terms
search_terms = swagbucks_bot.get_google_trends(400)

# Perform searches
swagbucks_bot.perform_searches(search_terms)

# Close the bot
swagbucks_bot.close()
