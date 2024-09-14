import webbrowser
import requests
from bs4 import BeautifulSoup
site="https://www.cricbuzz.com/"
req=requests.get(site)
soup=BeautifulSoup(req.content,"html.parser")

sites=[]
match_titles = []
match_link = []
text=[]
def scrape():
    s=BeautifulSoup(req.text, "html.parser")
    for i in s.find_all("a"): #All a gulote enter korbe
        try:
            href=i.attrs['href'] #a er vetor gea href attributes ber kore anbe
            if href.startswith("/"):
                sites.append(site+href)
        except: continue

    site_live = 'https://www.cricbuzz.com/cricket-match/live-scores'
    requ=requests.get(site_live)
    soupy=BeautifulSoup(requ.content,"html.parser")
    live_scores=soupy.find('div', {'class':'cb-col cb-col-100 mrgn-btm-5'})
    live_scores=live_scores.find('nav', {'class':"cb-mat-mnu"}).find_all("a")
    for tag in live_scores:
        if tag.has_attr('href'): match_link.append(site[:-1]+str(tag['href']))
        if tag.has_attr('title'):
            match_titles.append((tag['title']).lower())
        try:  text.append(tag.text.lower())
        except: continue

scrape()

def website(command):
  if 'match' in command: command.remove('match')
  if 'vs' in command: command.remove('vs')
  try:
    if 'score' in command or 'scores' in command:
        webbrowser.open('https://www.cricbuzz.com/cricket-match/live-scores')
    elif 'schedule' in command or 'day' in command :
        webbrowser.open('https://www.cricbuzz.com/cricket-schedule/upcoming-series/international')
    elif 'team' in command:
        webbrowser.open('https: // www.cricbuzz.com / cricket - team')
    elif 'recent' in command:
            webbrowser.open('https://www.cricbuzz.com/cricket-match/live-scores/recent-matches')
    elif 'upcoming' in command:
            webbrowser.open('https://www.cricbuzz.com/cricket-match/live-scores/upcoming-matches')
    elif 'series' in command:
        webbrowser.open("https://www.cricbuzz.com/cricket-schedule/series")
    elif 'archive' in command or 'archives' in command:
        webbrowser.open('https://www.cricbuzz.com/cricket-scorecard-archives')
    else:
        x=1
        for i in command:
              if x==0: break
              for j in text:
                if i in j:
                    index=text.index(j)
                    webbrowser.open(match_link[index])
                    x=0
                    break
        x=1
        for i in command:
              if x==0: break
              for j in match_titles:
                if i in j:
                    index=match_titles.index(j)
                    webbrowser.open(match_link[index])
                    x=0
                    break
  except: pass


