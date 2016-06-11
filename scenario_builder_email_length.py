__author__ = 'Kiryl Trembovolski'

from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def xpath_finder_wrapper(link):
    while True:
        try:
            output = driver.find_element_by_xpath(link)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def login(username, password):

    username_button = driver.find_element_by_id("login-username")
    password_button = driver.find_element_by_id("login-password")
    login_button = driver.find_element_by_id("login-button")

    username_button.send_keys(username)
    password_button.send_keys(password)

    time.sleep(1)

    login_button.click()

    time.sleep(6)

    scenarios_button = xpath_finder_wrapper("//div[text()='Scenarios']")

    scenarios_button.click()

    time.sleep(20)

def add_scenario_code(word, scenario_script):

    scenario_code = xpath_finder_wrapper("//textarea[@class='v-textarea v-widget v-textarea-error v-form-field v-textarea-v-form-field v-textarea-required v-required v-has-width']")
    scenario_code.send_keys(scenario_script % word.lower())

    time.sleep(2)

def add_scenario_name(word, count):

    scenario_name = xpath_finder_wrapper("//input[@class='v-textfield v-widget v-textfield-error v-form-field v-textfield-v-form-field v-textfield-required v-required v-has-width']")
    scenario_name.send_keys("email_length_" + word + str(count))

    time.sleep(2)

def choose_me_group(me_group):

    me_group_button = xpath_finder_wrapper("//select[@class='v-select-twincol-options']/option[text()='%s']" % me_group)
    me_group_button.click()

    time.sleep(2)

    choose_me_group_button = xpath_finder_wrapper("//div[@class='v-select-twincol-buttons']/div[1]")
    choose_me_group_button.click()

    time.sleep(2)

    save_changes_button = xpath_finder_wrapper("//span[text()='save changes']")
    save_changes_button.click()

    time.sleep(2)

def add_scenario(word, scenario_script, count):

    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='v-actionbar v-widget open v-actionbar-open v-has-height']/div[2]/ul/li[1]/span[2]")))

    # add_button = xpath_finder_wrapper("//section[@class='v-actionbar v-widget open v-actionbar-open v-has-height']/div[2]/ul/li[1]/span[2]")
    time.sleep(4)

    element.click()

    time.sleep(4)

    add_scenario_code(scenario_script)

    add_scenario_name(word, count)

    me_groups_button = xpath_finder_wrapper("//div[@class='dialog-root v-widget dialog-panel dialog-root-dialog-panel v-has-width v-has-height']/div/div[2]/div/div[2]/div/ul/li[2]/div[1]")
    me_groups_button.click()

    time.sleep(2)
    choose_me_group(me_group)

def add_scenario_code(scenario):
    scenario_code = xpath_finder_wrapper(
        "//textarea[@class='v-textarea v-widget v-textarea-error v-form-field v-textarea-v-form-field v-textarea-required v-required v-has-width']")
    scenario_code.send_keys(scenario)

    time.sleep(2)

if __name__ == '__main__':


    scenario_script = ['ContentFeature(name = "EmailLengthFeatureType", value > "10") AND ContentFeature(name = "EmailLengthFeatureType", value < "100")', 'ContentFeature(name = "EmailLengthFeatureType", value > "10") AND ContentFeature(name = "EmailLengthFeatureType", value < "120")', 'ContentFeature(name = "EmailLengthFeatureType", value > "10") AND ContentFeature(name = "EmailLengthFeatureType", value < "140")', 'ContentFeature(name = "EmailLengthFeatureType", value > "10") AND ContentFeature(name = "EmailLengthFeatureType", value < "160")']

    me_group = "Test"

    driver = webdriver.Chrome("/Users/anabaez/Google Drive/Tullett Prebon/Scenarios/scripts/chromedriver")
    driver.get("http://10.239.2.131:8081/admin/.magnolia/admincentral#app:beh-security:;/:treeview:")

    login("k.trembovolski", "Behavox2015")

    #cycle starts here
    start_time = time.time()

    for scenario in scenario_script:
        time.sleep(2)
        idx = 22 + scenario_script.index(scenario)
        add_scenario(str(idx), scenario, idx)

    finish_time = time.time()-start_time

    print "Execution time: ", finish_time/float(60)

    driver.quit()