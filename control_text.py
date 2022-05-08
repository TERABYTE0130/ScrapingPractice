from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

url = "https://www.google.com/"
keyword = "スクレイピング"

def main():
  option = Options()
  option.add_argument("--incognito")
  driver = webdriver.Chrome(options=option)
  driver.get(url)
  time.sleep(3)
  search = driver.find_element_by_name("q")
  search.send_keys(keyword)
  search.submit()
  soup = BeautifulSoup(driver.page_source,"html.parser")
  results = soup.find_all("h3", attrs={"class": "LC20lb"})
  for i, result in enumerate(results):
    text = result.get_text()
    print(f"{i}:{text}")
    
  time.sleep(5)
  driver.quit()

if __name__ == "__main__":
  exit(main())