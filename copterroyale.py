from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import datetime
import time
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument(r"--user-data-dir=C:/Users/ahpye/AppData/Local/Google/Chrome/User Data/") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# chrome_options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
# chrome_options.add_argument("--headless")
import time
import clipboard


PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
start_time = time.time()

driver.get("https://www.coolmathgames.com/0-copter-royale")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.execute_script("scroll(0, 330)")

driver.execute_script("cmg_remove_padg()")

driver.implicitly_wait(7)

driver.switch_to.frame(driver.find_element_by_id("html5game"))
actions = ActionChains(driver) #initialize ActionChain object

driver.implicitly_wait(2)

time.sleep(10)

root = driver.find_element_by_xpath("/html")

def newName():
    driver.execute_script("defly.generateUsername()")
    return

def getName():


    actions.move_by_offset(500, 430).click_and_hold().move_by_offset(170,0).release().perform()

    root.send_keys(Keys.LEFT_CONTROL, 'C')

    actions.move_by_offset(-670, -430).click().perform()

    print(clipboard.paste())

    if clipboard.paste() == "Fabulous Falcon":
        print("--- %s seconds ---" % (round(time.time() - start_time, 2)))


    return clipboard.paste()


def check():
    if getName() == "Fabulous Falcon":
        print("We did it!")
        return True
    else:
        return False


while getName() != "Fabulous Falcon":
    newName()
