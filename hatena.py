from cgitb import text
from turtle import write
import requests
from bs4 import BeautifulSoup
import csv

url = "https://b.hatena.ne.jp"

def save_csv(text_list):
  with open("output.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(text_list)

def main():
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  top_entries = soup.find("section",attrs={"class":"entrylist-unit"})
  entries = top_entries.find_all("div", attrs={"class":"entrylist-contents"})
  for entry in entries:
    title_tag = entry.find("h3", attrs={"class":"entrylist-contents-title"})
    title = title_tag.find("a").get("title")
    print(title)
    
    
if __name__ == "__main__":
  exit(main())
  
