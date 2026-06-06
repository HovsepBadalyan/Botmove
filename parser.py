from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time


def parse_move():
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # for Chrome >= 109

    driver = webdriver.Chrome(options=chrome_options)

    

    try:
        driver.get(url='https://www.imdb.com/chart/top/')
        time.sleep(3)
        # driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/div[3]/div[2]/div/button').click()
        # time.sleep(3)
        
        Drama = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/div[2]/ul').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/span/div/span/span[1]').text
        
        War = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[23]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[23]/div/div/div/div/div[2]/span/div/span/span[1]').text
        
        Crime = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/span/div/span/span[1]').text
        Thriller = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[3]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[3]/div/div/div/div/div[2]/span/div/span/span[1]').text
        PsychologicalThriller = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[13]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[13]/div/div/div/div/div[2]/span/div/span/span[1]').text 
        ActionEpic = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[33]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[33]/div/div/div/div/div[2]/span/div/span/span[1]').text
        Docudrama = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[48]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[48]/div/div/div/div/div[2]/span/div/span/span[1]').text
        Mystery = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[52]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[52]/div/div/div/div/div[2]/span/div/span/span[1]').text
        Comedy = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[85]/div/div/div/div/div[2]/div[2]/ul/div/a/h4').text, driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[85]/div/div/div/div/div[2]/span/div/span/span[1]').text
        
        return [Drama, War, Crime, Thriller, PsychologicalThriller, ActionEpic, Docudrama, Mystery, Comedy]
    
    except Exception as ex:
        return ex.__class__.__name__
        

    finally:
        driver.close()
        driver.quit()
        

