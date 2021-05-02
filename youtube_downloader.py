from selenium import webdriver
import time
import urllib.request 
import progressbar

url = input("enter the url\n")
pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

mobile_emulation = { "deviceName": "iPhone 6/7/8" }
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

path = r"D:\\Chromedriver.exe" #path of the chromedriver

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(path,options=chrome_options) 
driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.refresh()
element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/video')
video_source = element.get_attribute('src')
get_title = driver.title
driver.close()
urllib.request.urlretrieve(video_source, f'{get_title}.mp4',show_progress) 
print("video is downloaded")