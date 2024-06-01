import datetime
from bs4 import BeautifulSoup
import requests

#Текущая дата
def monthh():
    current_month = ""
    crm = str(datetime.date.today())
    crm = str(crm[5:7])
    if crm == "01":
        current_month = "Янв"
    elif crm == "02":
        current_month = "Фев"
    elif crm == "03":
        current_month = "Мар"
    elif crm == "04":
        current_month = "Апр"
    elif crm == "05":
        current_month = "мая"
    elif crm == "06":
        current_month = "Июн"
    elif crm == "07":
        current_month = "Июл"
    elif crm == "08":
        current_month = "Авг"
    elif crm == "09":
        current_month = "Сен"
    elif crm == "10":
        current_month = "Окт"
    elif crm == "11":
        current_month = "Ноя"
    elif crm == "12":
        current_month = "Дек"
    return current_month

def data():
    current_date = str(datetime.date.today())
    year = current_date[:4]
    month = monthh()
    day = current_date[8:]
    current_date = "            " + day + " " + month + " " + year + "           "
    return current_date

matchdates = data()
matches_string = []
matches = {}
#Матчи в текущий день
def matchestoday(league):
    global matchdate
    global matches_string
    global matches
    match_team_1 = []
    match_team_2 = []
    matchtime = []
    matchdate = []
    url = league
    page = requests.get(url)
    target_date = matchdates
    soup = BeautifulSoup(page.text, "html.parser")
    datte = soup.find_all('span', class_="match_date")
    time = soup.find_all('span', class_="match_time")
    team1 = soup.find_all('span', class_="match_team1")
    team2 = soup.find_all('span', class_="match_team2")
    stativen_daten = []
    for i in team1:
        d = i.text
        match_team_1.append(d)
    for i in team2:
        d = i.text
        match_team_2.append(d)
    for i in time:
        d = i.text
        matchtime.append(d)
    for i in datte:
        d = i.text
        matchdate.append(d)
    for i in range(len(time)):
        top = str(matchtime[i]) + " " + str(match_team_1[i]) + " против " + str(match_team_2[i])
        matches_string.append(top)
    for i in range(len(datte)):
        top = str(matchdate[i])
        stativen_daten.append(top)
    for i in range(len(stativen_daten)):
        cleaned_list = [s[s.find("'\n") + len("'\n' "):s.find("'")] for s in stativen_daten]
    for i in range(len(cleaned_list)):
        matches[cleaned_list[i]] = matches_string[i]
    matches_today = {}
    for i in matches:
        if i == target_date:
            matches_today[i] = matches[i]
            print(matches_today[i])
    matchess = ""
    for i in matches_today:
        matchess += i + matches_today[i] + "\n"
    return matchess
matchestoday("https://www.readfootball.com/football-spain/tournaments/primera/calendar.html")