from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep


class FreeRiceBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://freerice.com')
        sleep(2)

        #toggle menu
        self.driver.find_element_by_class_name("toolbar__menu-toggle-icon").click()
        sleep(0.5)

        #toggle login
        self.driver.find_element_by_xpath('//*[@id="root"]/nav/div/div[1]/div/div[2]/a[1]').click()
        sleep(0.5)

        #enter username and password
        self.driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("lakreiss")
        self.driver.find_element_by_xpath('//*[@id="login-password"]').send_keys("***************")

        #log in
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/button').click()

    def get_rice(self):
        #toggles menu
        self.driver.find_element_by_class_name("toolbar__menu-toggle-icon").click()
        sleep(0.5)

        #toggles category
        self.driver.find_element_by_xpath('//*[@id="root"]/nav/div/nav/ul/li[2]/a').click()
        sleep(0.5)

        #toggles math multiplication
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/div[6]/div[1]/div[1]').click()

        self.infinite_loop()

    def infinite_loop(self):
        while(True):
            try:
                sleep(.1)
                #accesses and solves the math problem
                problem = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[1]')
                problem_text = problem.get_attribute('innerHTML')
                numbers = problem_text.split(' x ')
                num_1, num_2 = int(numbers[0]), int(numbers[1])
                product = num_1 * num_2

                #test each button
                n = 1
                button = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[2]')
                button_answer = int(button.get_attribute('innerHTML'))
                if (button_answer == product):
                    print("button ", n, ":", button_answer)
                    button.click()
                else:
                    n += 1
                    button = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[3]')
                    button_answer = int(button.get_attribute('innerHTML'))
                    if (button_answer == product):
                        print("button ", n, ":", button_answer)
                        button.click()
                    else:
                        n += 1
                        button = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[4]')
                        button_answer = int(button.get_attribute('innerHTML'))
                        if (button_answer == product):
                            print("button ", n, ":", button_answer)
                            button.click()
                        else:
                            n += 1
                            button = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[5]')
                            button_answer = int(button.get_attribute('innerHTML'))
                            if (button_answer == product):
                                print("button ", n, ":", button_answer)
                                button.click()
                            else:
                                print("failed")
            except NoSuchElementException:
                print("NoSuchElementException, trying again")
            except StaleElementReferenceException:
                print("StaleElementReferenceException, trying again")
            except ElementClickInterceptedException:
                print("ElementClickInterceptedException, trying again")
            except ElementNotInteractableException:
                print("ElementNotInteractableException, trying again")
            # except NoSuchWindowException: #this one might be good to not catch
            #     print("NoSuchWindowException, trying again")


bot = FreeRiceBot()
bot.login()
bot.get_rice()
