__author__ = 'Ana Baez'

from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import csv

def xpath_finder_wrapper(link):
    while True:
        try:
            output = driver.find_element_by_xpath(link)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def xpath_finder_elements_wrapper(link):
    while True:
        try:
            output = driver.find_elements_by_xpath(link)
            if len(output) != 2:
                continue
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def login(username, password):

    login_button = driver.find_element_by_id("username")
    password_button = driver.find_element_by_id("password")
    submit_button = driver.find_element_by_id("submit")

    login_button.send_keys(username)
    password_button.send_keys(password)

    time.sleep(1)

    submit_button.click()

    time.sleep(4)

def search():

    #find where to insert search in page
    search_field = xpath_finder_wrapper("//input[@class='v-textfield v-widget filter-panel-keywords-field v-textfield-filter-panel-keywords-field']")
    # type in search value
    search_field.send_keys(search_value)

    time.sleep(2)
    # run query by pressing search icon
    search_field_submit = xpath_finder_wrapper("//div[@class='v-button v-widget search-button v-button-search-button']")
    search_field_submit.click()

    time.sleep(6)

if __name__ == '__main__':

    driver = webdriver.Chrome("/Users/anabaez/Google Drive/Tullett Prebon/Scenarios/scripts/chromedriver")
    driver.get("http://130.211.65.247:18081/dashboard/secure/dashboard#!search")

    fp_ids = {}
    scenarios = ['noise_200']
    search_value = "scenario:noise_800"
    buffer_id = ""
    buffer_name = ""
    name = ""

    flag = False
    flag_finish = True

    time.sleep(1)

    login("user", "rulethemall")

    # initilise / find the search field
    search_field = xpath_finder_wrapper("//input[@class='v-textfield v-widget filter-panel-keywords-field v-textfield-filter-panel-keywords-field']")
    search_field.send_keys(search_value)

    time.sleep(3)

    # submit query to search field
    search_field_submit = xpath_finder_wrapper("//div[@class='v-button v-widget search-button v-button-search-button']")
    search_field_submit.click()

    time.sleep(20)

    #get the total number of hits
    total_count = xpath_finder_wrapper("//div[@class='v-label v-widget stats-label v-label-stats-label v-has-width']")
    count = total_count.text.split(' ', 3)[3]

    print("Total hits:.{}".format(total_count))
    start_time = time.time()
    for i in range(20000):
    #iteration by names

        if flag is True:
            break
        #navegate to the names list
        names_path = "//div[@id='left-container']/div[2]/div[1]/div[3]/table/tbody/tr"
        names = driver.find_elements_by_xpath(names_path)

        if flag_finish is True:
            buffer_name = name

            #get count of emails per name in container
            name = str(names[i].text.split('(',3)[0][:-1])
            contents_num = names[i].text.split(' ',4)[-1][1:-1]
        else:
            buffer_name = name
            name = str(names[len(names)-1].text.split('(', 3)[0][:-1])
            contents_num = names[len(names)-1].text.split(' ', 4)[-1][1:-1]

        if name == buffer_name:
            break

        fp_ids[str(name)] = []

        time.sleep(6)

        #load all buttons and click 'all' button
        all_buttons = xpath_finder_elements_wrapper("//div[@class='v-link v-widget load-more-link v-link-load-more-link']")

        all_buttons[1].click()

        if name == str("Other"):

            path = "//div[@id='top-container']/div[1]/div[1]/div[1]/div[3]/table/tbody/tr[" + str(1) + "]/td[5]"

            time.sleep(3)

            content = xpath_finder_wrapper(path)

            content.click()

        contents_count = driver.find_elements_by_xpath("//div[@id='top-container']/div[1]/div[1]/div[1]/div[3]/table/tbody/tr")

        for j in range(int(contents_num)):
        #iteration by contents for one contact

            time.sleep(2)
            #find and click show more button
            show_more_button = xpath_finder_wrapper("//div[@class='v-button v-widget link v-button-link']")
            show_more_button.click()

            time.sleep(2)

            # extract message ID
            id = xpath_finder_wrapper("//div[@class='v-verticallayout v-layout v-vertical v-widget v-has-width v-margin-top v-margin-right v-margin-bottom v-margin-left']/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[3]/div")
            print str(id.text)

            if buffer_id == str(id.text) and buffer_name == name:
                flag = True
                fp_ids[name].append(str(id.text))
                break
            else:
                buffer_id = str(id.text)

            #add ID to list
            fp_ids[name].append(str(id.text))
            print len(fp_ids[name])

            #close more info window
            close_button = xpath_finder_wrapper("//div[@class='v-window-closebox']")

            time.sleep(2)

            close_button.click()

            print(contents_num)
            if j is int(contents_num)-1:
                break

            if j >= len(contents_count):
                j_plus_one = len(contents_count)
            else:
                j_plus_one = j + 1

            path = "//div[@id='top-container']/div[1]/div[1]/div[1]/div[3]/table/tbody/tr[" + str(j_plus_one) + "]/td[5]"

            time.sleep(2)

            content = xpath_finder_wrapper(path)

            actionsTmp = webdriver.ActionChains(driver).move_to_element(content)
            actionsTmp.click().perform()

            actions = webdriver.ActionChains(driver)
            time.sleep(2)
            actions.send_keys(Keys.ARROW_DOWN).perform()

        if i >= len(names)-1:
            i_plus_one = len(names)
            flag_finish = False

            if flag is True:
                break
        else:
            i_plus_one = i + 1
        next_name_path = names_path + "[" + str(i_plus_one) + "]/td"

        time.sleep(2)

        nameLine = xpath_finder_wrapper(next_name_path)

        actionsTmp = webdriver.ActionChains(driver).move_to_element(nameLine)
        actionsTmp.click().perform()

        actions = webdriver.ActionChains(driver)
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).perform()

    time_finish = time.time() - start_time

    print time_finish/float(60), "Execution time: "
    for i in fp_ids:
        print i, fp_ids[i]

    writer = csv.writer(open('/Users/anabaez/Google Drive/Tullett Prebon/Scenarios/scripts/%s.csv' % search_value, 'wb'))
    for key, value in fp_ids.items():
        writer.writerow([key, value])

    time.sleep(3)

    driver.quit()