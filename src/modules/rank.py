from selenium import webdriver
import requests
from bs4 import BeautifulSoup


class GetRank:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
 
    path = "C:\\Users\\David Kim\\Searches\\Downloads\\chromedriver_win32\\chromedriver.exe" #webdriver 설치 경로를 입력해주세요
    driver = webdriver.Chrome(path,chrome_options=options)
    driver.implicitly_wait(3) # seconds

    naver_wfootball = "https://sports.news.naver.com/wfootball/record/index.nhn?category=bundesliga&year=2019"
    driver.get(naver_wfootball)
 
    page = driver.page_source
    premi_team_rank_list =  BeautifulSoup(page,"html.parser")
    team_rank_list = premi_team_rank_list.select('#wfootballTeamRecordBody>table>tbody>tr')

    for team in team_rank_list:
        num = team.select('.num > div.inner > strong')[0].text
        name = team.select('.name')[0].text
        m = team.select('td')[2]
        w = team.select('td')[4]
        d = team.select('td')[5]
        l = team.select('td')[6]
        g = team.select('td')[7]
        c = team.select('td')[8]
        d = team.select('td')[9]
        match = m.select('div.inner > span')[0].text
        win = w.select('div.inner > span')[0].text
        draw = d.select('div.inner > span')[0].text
        lose = l.select('div.inner > span')[0].text
        goal = g.select('div.inner > span')[0].text      
        concede = c.select('div.inner > span')[0].text
        difference = d.select('div.inner > span')[0].text
        score = team.select('.selected > div.inner > span')[0].text
        fw = open("새파일.txt", "a+", encoding='utf-8')
        fw.write(f"「{num}위 : {name}  경기수: {match}  승점 : {score}점  승 : {win}승  무 : {draw}무  패 : {lose}패  득점 : {goal}점  실점 : {concede}점  득실차 : {difference}점」\n")

    fw.close()

# 4 : 승 , 5 : 무, 6 : 패, 7 : 득점, 8 : 실점, 9 : 득실차
# concede