from selenium import webdriver
import requests
from bs4 import BeautifulSoup

class Schedule:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    path = "C:\\Users\\David Kim\\Searches\\Downloads\\chromedriver_win32\\chromedriver.exe" #webdriver 설치 경로를 입력해주세요
    driver = webdriver.Chrome(path,chrome_options=options)
    driver.implicitly_wait(3) # seconds

    naver_wfootball = "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=07&category=seria"
    driver.get(naver_wfootball)

    page = driver.page_source
    team_day =  BeautifulSoup(page,"html.parser")
    team_day_list = team_day.select('.schedule_month_table>table>tbody>tr')
    fw = open("schedule.txt", "a+", encoding='utf-8')

    for schedule in team_day_list:
        with open("schedule.txt", "a+", encoding='utf-8') as fw:
            fw.flush()
            try:
                day = schedule.select('th > div.inner > em')[0].text
                fw.write(f"날짜 : {day}일\n")
            except IndexError:
                pass
            try:
                time = schedule.select('.time_place > div.inner > span.time')[0].text
                fw.write(f"시간 : {time} ")
            except IndexError:
                pass
            try:
                team_left = schedule.select('.team_left > span.name')[0].text
                team_left_score = schedule.select('.team_left > span.score')[0].text
                team_right_score = schedule.select('.team_right > span.score')[0].text
                team_right = schedule.select('.team_right > span.name')[0].text
                fw.write(f"{team_left} {team_left_score} : {team_right_score} {team_right} \n")
            except IndexError:
                try:
                    team_left = schedule.select('.team_left > span.name')[0].text
                    team_right = schedule.select('.team_right > span.name')[0].text
                    fw.write(f"{team_left} vs {team_right} \n")
                except IndexError:
                    pass    