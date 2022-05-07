from cgitb import text
from turtle import write
import requests
from bs4 import BeautifulSoup
import csv

url = "https://ja.wikipedia.org/"

def save_csv(text_list):
  with open("output.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(text_list)

def main():
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  today_list = []
  today = soup.find("div",attrs={"id": "on_this_day"})
  entries = today.find_all("li")
  for entry in range(len(entries)):
    today_list.append([entry,entries[entry].get_text()])    
  save_csv(today_list)
  

if __name__ == "__main__":
  exit(main())
  
