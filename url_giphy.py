import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def startit():
    driver = webdriver.Chrome(executable_path='/Users/xinyue/PycharmProjects/web_scraping/driver/chromedriver')
    driver.get('https://giphy.com/explore/confusing')
    driver.maximize_window()
    df = pd.DataFrame(columns=['image_url','image_tag'])
    stop_num = 0
    counter = 0
    while True:
        driver, stop_num, sub_df,counter = collect_img(driver, stop_num,counter)
        df = df.append(sub_df, ignore_index=True)
        df.to_csv('giphy.csv')
        time.sleep(3)



def collect_img(driver,stop_num,counter):
    df = pd.DataFrame(columns=['image_url', 'image_tag'])
    image_list = driver.find_elements_by_xpath('//*[@id="react-target"]/div/div[5]/div/div[1]/a')


    for each_img in image_list[stop_num:]:
        image_url = each_img.find_element_by_xpath('.//div/img').get_attribute('src')
        image_tag = each_img.find_elements_by_xpath('.//div/div[2]/span')
        if image_url == 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7':
            actions = ActionChains(driver)
            actions.move_to_element(each_img).perform()
            return driver, stop_num, df,counter

        tag_list = []
        for each_tag in image_tag:
            tag = each_tag.get_attribute('textContent')
            tag_list.append(tag)
        data = {'image_url': image_url, 'image_tag':tag_list}
        df = df.append(data,ignore_index=True)
        stop_num = stop_num+1
    end_numb = counter*650
    driver.execute_script("window.scrollTo(0, "+str(end_numb)+")")
    counter = counter+1
    return driver, stop_num, df,counter


startit()