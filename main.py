import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException
from openpyxl import Workbook
from selenium.webdriver.common.by import By
import pandas as pd
import os
import requests
from selenium.webdriver.common.keys import Keys
import pyautogui as pt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def exporter(element_list):
    if element_list:
        return element_list[0].text
    return ""

workbook = Workbook()
sheet = workbook.active

start_time = time.time()

cService = ChromeService(executable_path=r'C:\Users\Ahmet\Desktop\masaüstü\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
result = []


driver.get("http://212.237.53.207/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

time.sleep(3)


# Zoom out 
driver.refresh()
time.sleep(2)
pt.keyDown("ctrl")
pt.press("-")
pt.press("-")
pt.press("-")
pt.press("-")
pt.press("-")
pt.press("-")
pt.keyUp("ctrl")
driver.find_element("xpath","/html/body/div[1]/div/div/div[3]/a").click()


time.sleep(2)

# Login to the website
driver.find_element("xpath", "/html/body/header/nav/ul/li[6]/a").click()
time.sleep(4)
driver.find_element("name","email").send_keys("email") # Change this with your account's email
driver.find_element("name","password").send_keys("password") # Change this with your account's password
driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div/div/div[2]/form/div[4]/div/button").click()
time.sleep(4)

driver.find_element("xpath", "/html/body/header/nav[1]/ul/li[2]/a").click() #hocametreye tıklama

driver.find_element("xpath", "/html/body/main/div[1]/div/div[3]/div[3]/div[2]/form/span/span[1]/span/span[1]").click()#hoca seçiciye tıklama

time.sleep(4)  # Açılması için bekle

# Tüm seçenekleri bul
options = driver.find_elements(By.CSS_SELECTOR, "li.select2-results__option")

# Seçenekleri yazdır
names_list = [f'{option.text}' for option in options]


# Open the website
driver.get("http://212.237.53.207/")

time.sleep(3)

driver.refresh()
time.sleep(2)

driver.find_element("xpath", "/html/body/header/nav[1]/ul/li[2]/a").click()#hocametreye tıklama

# Initialize a variable for counting instructors
hoca_counter =0

time.sleep(1)
driver.find_element("xpath", "/html/body/main/div[1]/div/div[3]/div[3]/div[2]/form/a").click()#aramaya tıklama 



time.sleep(2)

main_div = driver.find_element("class name", 'panel-body')
main_folder = r'C:\Users\Ahmet\Desktop\masaüstü\notkutusulatest'
# Altındaki div'leri bulun ve sayısını öğrenin
sub_divs = driver.find_elements("class name", 'col-md-4 col-sm-6 col-xs-3')
print(f'Alt div sayısı: {len(sub_divs)}')

while hoca_counter < 1000:

    driver.find_element("xpath", "/html/body/main/div[1]/div/div[3]/div[3]/div[2]/form/span/span[1]/span/span[1]").click()#hoca seçiciye tıklama
    time.sleep(.12)

    if hoca_counter == 322: # This instructors name is bugged on website so we have to manually send her name
        driver.find_element("xpath","/html/body/span/span/span[1]/input").send_keys("esra")
    else:
        driver.find_element("xpath","/html/body/span/span/span[1]/input").send_keys(names_list[hoca_counter-1])
    
    time.sleep(.05)
    
    driver.find_element("xpath","/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    
    # Initialize variables and create folder for each instructor
    faculty  = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/p").text
    name  = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/h3").text
    folder_name = faculty +" " +name 
    print(folder_name)
    path_for_teacher_names = os.path.join(main_folder,folder_name)
    os.makedirs(path_for_teacher_names,exist_ok=True)
    rate1 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/div").text
    average1 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/i").text
    rate3 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div").text
    average3 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/i").text
    rate4 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div[3]/div").text
    average4 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div[3]/i").text
    rate5 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[4]/div/div[3]/div").text
    average5 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[4]/div/div[3]/i").text
    rate6 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[5]/div/div[3]/div").text
    average6 = driver.find_element("xpath","/html/body/main/div[1]/div/div[2]/div/div[1]/div/div[2]/div[5]/div/div[3]/i").text
    print(rate1)
    print(average1)
    # Try to show more comments about instructor
    try:
        driver.find_element("id","show-more-comment").click()
        try:
            driver.find_element("id","show-more-comment").click()
            try:
                driver.find_element("id","show-more-comment").click()
                try:
                    driver.find_element("id","show-more-comment").click()
                    try:
                        driver.find_element("id","show-more-comment").click()
        
                    except:
                        print("daha fazla göster tuşu mevcut değil")
                except:
                    print("daha fazla göster tuşu mevcut değil")
            except:
                print("daha fazla göster tuşu mevcut değil")
        except:
            print("daha fazla göster tuşu mevcut değil")
    except:
        print("daha fazla göster tuşu mevcut değil")

    comments = driver.find_elements("class name","each-comment-row")
    print("yorum sayısı")
    print(len(comments))



    # comment kısımlarını açma
    for l in range (1,15):
        xpath= f'/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[{l}]/div[1]/div[2]/p/a'

        try:
            clickme= driver.find_element("xpath",xpath)
            try:
                clickme = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                clickme.click()
            except:
                print("not clickable")


        except NoSuchElementException:
            print(f"Element does not exist: {xpath}")        

    for i in range(1, 20):  # Adjust range as needed
        xpath = f'/html/body/main/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[{i}]/a'
        try:
            element = driver.find_element("xpath", xpath)
            print(f"Element exists: {xpath}")
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            
            folder2_name = element.text
            element = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
            element.click()
            
            path_for_class_names = os.path.join(path_for_teacher_names, folder2_name)
            os.makedirs(path_for_class_names, exist_ok=True)

            images = driver.find_elements("xpath", "//img[@data-toggle='modal' and @width='100' and @height='100']")
            print(len(images))

            # Download each image
            for j, img in enumerate(images):
                img_url = img.get_attribute('src')
                if img_url:
                    try:
                        img_data = requests.get(img_url).content
                        img_name = os.path.join(path_for_class_names, f'image_{j+1}.jpg')
                        with open(img_name, 'wb') as handler:
                            handler.write(img_data)
                        print(f'Downloaded {img_name}')
                    except requests.RequestException as e:
                        print(f"Failed to download image {j+1}: {e}")

            time.sleep(0.7)
            driver.back()

        except NoSuchElementException:
            print(f"Element not found: {xpath}")
        except ElementClickInterceptedException:
            print(f"Element could not be clicked: {xpath}")
        except Exception as e:
            print(f"An error occurred: {e}")



    if len(comments) == 0:
        comment1 = "None"
        comment2 = "None"
        comment3 = "None"
        comment4 = "None"
        comment5 = "None"
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 1:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = "None"
        comment3 = "None"
        comment4 = "None"
        comment5 = "None"
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)
    elif len(comments) == 2:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = "None"
        comment4 = "None"
        comment5 = "None"
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)    
    elif len(comments) == 3:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        comment4 = "None"
        comment5 = "None"
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15


    }
        result.append(temp_data)
        print("inside 3")
    elif len(comments) == 4:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")

        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        comment5 = "None"
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 5:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")

        # Default values for comments beyond the fifth one
        comment6 = "None"
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 6:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")

        # Default values for comments beyond the sixth one
        comment7 = "None"
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum sayısı" : len(comments),
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15
    }
        result.append(temp_data)

    elif len(comments) == 7:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")

        # Default values for comments beyond the seventh one
        comment8 = "None"
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 8:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")
        
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")

        # Default values for comments beyond the eighth one
        comment9 = "None"
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 9:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")
        
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")
        
        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")

        # Default values for comments beyond the ninth one
        comment10 = "None"
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)
    elif len(comments) == 10:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"
        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 10:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")
        
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")
        
        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")
        
        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        # Default values for comments beyond the tenth one
        comment11 = "None"
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 11:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")
        
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")
        
        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")
        
        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        # Default values for comments beyond the eleventh one
        comment12 = "None"
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)

    elif len(comments) == 12:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")
        
        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")
        
        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")
        
        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")
        
        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")
        
        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")
        
        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")
        
        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")
        
        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")
        
        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[2]/div[2]/p").text
        if comment12.strip() == "":
            comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[1]/div[2]/p").text
            print("comment12 was blank")

        # Default values for comments beyond the twelfth one
        comment13 = "None"
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15
    }
        result.append(temp_data)

    elif len(comments) == 13:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")

        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")

        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")

        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")

        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")

        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")

        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")

        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")

        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")

        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[2]/div[2]/p").text
        if comment12.strip() == "":
            comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[1]/div[2]/p").text
            print("comment12 was blank")

        comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[2]/div[2]/p").text
        if comment13.strip() == "":
            comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[1]/div[2]/p").text
            print("comment13 was blank")

        # Default values for comments beyond the thirteenth one
        comment14 = "None"
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15
    }
        result.append(temp_data)

    elif len(comments) == 14:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")

        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")

        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")

        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")

        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")

        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")

        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")

        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")

        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")

        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[2]/div[2]/p").text
        if comment12.strip() == "":
            comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[1]/div[2]/p").text
            print("comment12 was blank")

        comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[2]/div[2]/p").text
        if comment13.strip() == "":
            comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[1]/div[2]/p").text
            print("comment13 was blank")

        comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[2]/div[2]/p").text
        if comment14.strip() == "":
            comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[1]/div[2]/p").text
            print("comment14 was blank")

        # Default values for comments beyond the fourteenth one
        comment15 = "None"

        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15
    }
        result.append(temp_data)

    elif len(comments) == 15:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")

        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")

        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")

        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")

        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")

        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")

        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")

        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")

        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")

        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[2]/div[2]/p").text
        if comment12.strip() == "":
            comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[1]/div[2]/p").text
            print("comment12 was blank")

        comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[2]/div[2]/p").text
        if comment13.strip() == "":
            comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[1]/div[2]/p").text
            print("comment13 was blank")

        comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[2]/div[2]/p").text
        if comment14.strip() == "":
            comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[1]/div[2]/p").text
            print("comment14 was blank")

        comment15 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[15]/div[2]/div[2]/p").text
        if comment15.strip() == "":
            comment15 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[15]/div[1]/div[2]/p").text
            print("comment15 was blank")


        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15

    }
        result.append(temp_data)
    else:
        comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p").text
        if comment1.strip() == "":
            comment1 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/p").text
            print("comment1 was blank")

        comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/p").text
        if comment2.strip() == "":
            comment2 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/p").text
            print("comment2 was blank")

        comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/p").text
        if comment3.strip() == "":
            comment3 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/p").text
            print("comment3 was blank")

        comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]/p").text
        if comment4.strip() == "":
            comment4 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/div[2]/p").text
            print("comment4 was blank")

        comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/p").text
        if comment5.strip() == "":
            comment5 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/p").text
            print("comment5 was blank")

        comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/p").text
        if comment6.strip() == "":
            comment6 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div[2]/p").text
            print("comment6 was blank")

        comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div[2]/p").text
        if comment7.strip() == "":
            comment7 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[7]/div[1]/div[2]/p").text
            print("comment7 was blank")

        comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[2]/div[2]/p").text
        if comment8.strip() == "":
            comment8 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[8]/div[1]/div[2]/p").text
            print("comment8 was blank")

        comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[2]/div[2]/p").text
        if comment9.strip() == "":
            comment9 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[9]/div[1]/div[2]/p").text
            print("comment9 was blank")

        comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/p").text
        if comment10.strip() == "":
            comment10 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[10]/div[1]/div[2]/p").text
            print("comment10 was blank")

        comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[2]/div[2]/p").text
        if comment11.strip() == "":
            comment11 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[11]/div[1]/div[2]/p").text
            print("comment11 was blank")

        comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[2]/div[2]/p").text
        if comment12.strip() == "":
            comment12 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[12]/div[1]/div[2]/p").text
            print("comment12 was blank")

        comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[2]/div[2]/p").text
        if comment13.strip() == "":
            comment13 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[13]/div[1]/div[2]/p").text
            print("comment13 was blank")

        comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[2]/div[2]/p").text
        if comment14.strip() == "":
            comment14 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[14]/div[1]/div[2]/p").text
            print("comment14 was blank")

        comment15 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[15]/div[2]/div[2]/p").text
        if comment15.strip() == "":
            comment15 = driver.find_element("xpath", "/html/body/main/div[1]/div/div[2]/div/div[2]/div[2]/div/div[15]/div[1]/div[2]/p").text
            print("comment15 was blank")


        temp_data = {
        "Faculty" : faculty,
        "Name" : name,
        "Notu Bol mu" : rate1,
        "Notu Bol mu oy sayısı" : average1,
        "Yardımseverlik": rate3,
        "Yardımseverlik oy sayısı" : average3,
        "Ödev Verir mi": rate4,
        "Ödev Verir mi oy sayısı": average4,
        "Yoklama Alır mı": rate5,
        "Yoklama Alır mı bol sayısı" : average5,
        "Ders Anlatımı" : rate6,
        "Ders Anlatımı oy sayısı" : average6,
        "Yorum 1": comment1,
        "Yorum 2": comment2,
        "Yorum 3": comment3,
        "Yorum 4": comment4,
        "Yorum 5": comment5,
        "Yorum 6": comment6,
        "Yorum 7": comment7,
        "Yorum 8": comment8,
        "Yorum 9": comment9,
        "Yorum 10": comment10,
        "Yorum 11": comment11,
        "Yorum 12": comment12,
        "Yorum 13": comment13,
        "Yorum 14": comment14,
        "Yorum 15": comment15}        




            # Or extract some text:
            
            
            
            # Perform any other operations you need...

    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")

    pt.press("up")
    
    pt.press("up")
    pt.press("up")
    pt.press("up")
    pt.press("up")

    
    pt.press("up")
    pt.press("up")
    hoca_counter += 1
    sayaç = f"hoca sayacı {hoca_counter}"
    print(sayaç)
    print(sayaç)
    print(sayaç)
    print(sayaç)
    if (hoca_counter + 1) % 51 == 0:
        df_data = pd.DataFrame(result)
        print(df_data)
        filename = str(hoca_counter) + ".xlsx"
        df_data.to_excel(filename, index=False)
            

df_data = pd.DataFrame(result)
print(df_data)
filename = "final2.xlsx"
df_data.to_excel(filename, index=False)
        


# Find all image elements

# Close the WebDriver
driver.quit()