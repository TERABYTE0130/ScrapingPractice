import imp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

url = "https://twitter.com/i/flow/login"
usr = ""
password = ""
next_button_path = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]"
login_button_path = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div"

def main():
  option = Options()
  option.add_argument("--incognito")
  driver = webdriver.Chrome(options=option)
  driver.get(url)
  time.sleep(5)
  user_form = driver.find_element_by_name("text")
  user_form.send_keys(usr)
  next_button = driver.find_element_by_xpath(next_button_path)
  next_button.click()
  time.sleep(3)
  password_box = driver.find_element_by_name("password")
  password_box.send_keys(password)
  login_button = driver.find_element_by_xpath(login_button_path)
  login_button.click()
  time.sleep(10)

if __name__ == "__main__":
  exit(main())