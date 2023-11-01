#########SCRAPING TOP 100 HOT SONGS FROM BILLBOARD

from bs4 import BeautifulSoup
import requests
class Songs:
    def __init__(self):
        self.song_names=[]
        self.year=""
    def song_lists(self):
        date= input("Which year do you want to travel to? Type "
                      "the date in this format YYYY-MM-DD: ")
        self.year=date.split("-")[0]
        response=requests.get(url="https://www.billboard.com/charts/hot-100/"+date)
        if response.status_code==200:
            content=response.text
            soup=BeautifulSoup(content,"html.parser")
            text=soup.select("li ul li h3")
            text1=soup.select("li ul li span")
            self.song_names=[item.get_text().strip() for item in text]
            return self.song_names,self.year
        else:
            print("invalid requests")
