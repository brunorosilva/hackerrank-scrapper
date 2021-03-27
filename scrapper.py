from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import username, password
import os

class scrapper():
    def __init__(self, path='', options=ChromeOptions()):
        self.driver = Chrome(path, options=options)
        self.driver.get('https://www.hackerrank.com/auth/login')

    def _get_challenge_info(self):
        challenge_title = self._get_challenge_title()
        challenge_description = self._get_challenge_description()
        sleep(5)
        challenge_solution = self._get_challenge_solution()
        
        return challenge_title, challenge_description, challenge_solution

    def _get_challenge_title(self):
        return self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/header/div/div/div[1]/div/h1/div/h1').text

    def _get_challenge_description(self):
        try:
            descrp_html = self.driver.find_element_by_xpath('//*[@id="tab-3-content-undefined"]/div/div').get_attribute("outerHTML")
        except:
            descrp_html = self.driver.find_element_by_xpath('//*[@id="tab-4-content-undefined"]/div/div').get_attribute("outerHTML")
        return descrp_html

    def _get_challenge_solution(self):
        #try:
        solution = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[3]/div/section/div/div/div/div[1]/section[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]').text


        return solution
        
    def _save_info(self, tutorial_name, challenge_title, challenge_description, challenge_solution, extension):
        if not os.path.exists(tutorial_name):
            os.mkdir(tutorial_name)
        
        os.mkdir(tutorial_name + "/" + challenge_title)
        f_description = open(str(tutorial_name) + "/" + str(challenge_title) + "/description.html", 'w')
        f_description.write(challenge_description)
        f_description.close()


        f_solution = open(str(tutorial_name) + "/" + str(challenge_title) + "/solution." + extension, 'w')
        f_solution.write(challenge_solution)
        f_solution.close()
        print("Challenge", challenge_title, "saved successfully")


    def login(self, username, password):
        username_field_xpath = '//*[@id="input-1"]'
        password_field_xpath = '//*[@id="input-2"]'
        username_field = self.driver.find_element_by_xpath(username_field_xpath)
        password_field = self.driver.find_element_by_xpath(password_field_xpath)

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)


    def run(self, challenge_list_url, tutorial_name, extension):
        self.driver.get(challenge_list_url)
        sleep(5)

        # scroll to end of the page just to get all of the challenges
        lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            sleep(3)
            lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True


        challenges_list = self.driver.find_element_by_class_name('challenges-list')
        challenges_urls = [el.get_attribute('href') for el in challenges_list.find_elements_by_tag_name('a')]

        print(f"{len(challenges_urls)} Challenges where found")

        for i, challenge in enumerate(challenges_urls):
            try:
                self.driver.get(challenge)
                challenge_title, challenge_description, challenge_solution = self._get_challenge_info()
                self._save_info(tutorial_name, challenge_title, challenge_description, challenge_solution, extension)
                
            except Exception as e:
                print(f"The Challenge {i+1} Couldn't be retrevied")
                print(e)
            sleep(3)





### change this one to your need        

# if your driver is already in your path
# you won't need to worry with the path_to_driver
# variable, therefore just leave it as a empty string

challenge_list_url = 'https://www.hackerrank.com/domains/tutorials/10-days-of-javascript?filters%5Bsubdomains%5D%5B%5D=10-days-of-javascript&filters%5Bstatus%5D%5B%5D=solved&badge_type=10-days-of-javascript'
tutorial_name      = '10-days-of-javascript'
extension          = 'js'
path_to_driver     = 'chromedriver_linux64/chromedriver'

options = ChromeOptions()
options.add_argument('--start-maximized')
sc = scrapper(path_to_driver, options=options)
sc.login(username, password)
sleep(5)
sc.run(challenge_list_url, tutorial_name, extension)
sc.driver.close()