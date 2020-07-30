from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Schedule:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    path = "C:\\Users\\David Kim\\Searches\\Downloads\\chromedriver_win32\\chromedriver.exe" #webdriver 설치 경로를 입력해주세요
    driver = webdriver.Chrome(path,chrome_options=options)
    driver.implicitly_wait(3) # seconds

    year = datetime.today().year
    month = datetime.today().month
    today = datetime.today().day

    def this_match(self, league='epl', year=year, month=month, day=today):
        
        naver_wfootball = f"https://sports.news.naver.com/wfootball/schedule/index.nhn?year={year}&month={month}&category={league}"
        self.driver.get(naver_wfootball)

        page = self.driver.page_source
        team_day =  BeautifulSoup(page,"html.parser")
        team_day_list = team_day.select('.schedule_month_table>table>tbody>tr')

        tod = f"{month}.{day}"
        message = ""
        today_match_list = []
        for schedule in team_day_list:
            try:
                day = schedule.select('th > div.inner > em')[0].text
                if(day == tod):
                    message += f"^날짜 : {day}일\n"
            except IndexError:
                pass
            if(day == tod):
                try:
                    time = schedule.select('.time_place > div.inner > span.time')[0].text
                    message += f"시간 : {time} "
                except IndexError:
                    message += "경기가 없습니다\n"
                try:
                    team_left = schedule.select('.team_left > span.name')[0].text
                    team_left_score = schedule.select('.team_left > span.score')[0].text
                    team_right_score = schedule.select('.team_right > span.score')[0].text
                    team_right = schedule.select('.team_right > span.name')[0].text
                    message += f"{team_left} {team_left_score} : {team_right_score} {team_right} \n"
                except IndexError:
                    try:
                        team_left = schedule.select('.team_left > span.name')[0].text
                        team_right = schedule.select('.team_right > span.name')[0].text
                        message += f"{team_left} vs {team_right} \n"
                    except IndexError:
                        pass
        today_match_list = (message.split('^'))
        return today_match_list

    def today_match(self, league='epl'):
        year = datetime.today().year
        month = datetime.today().month
        today = datetime.today().day

        naver_wfootball = f"https://sports.news.naver.com/wfootball/schedule/index.nhn?year={year}&month={month}&category={league}"
        self.driver.get(naver_wfootball)

        page = self.driver.page_source
        team_day =  BeautifulSoup(page,"html.parser")
        team_day_list = team_day.select('.schedule_month_table>table>tbody>tr')

        tod = f"{month}.{today}"
        message = ""
        today_match_list = []
        for schedule in team_day_list:
            try:
                day = schedule.select('th > div.inner > em')[0].text
                if(day == tod):
                    message += f"^날짜 : {day}일\n"
            except IndexError:
                pass
            if(day == tod):
                try:
                    time = schedule.select('.time_place > div.inner > span.time')[0].text
                    message += f"시간 : {time} "
                except IndexError:
                    message += "경기가 없습니다\n"
                try:
                    team_left = schedule.select('.team_left > span.name')[0].text
                    team_left_score = schedule.select('.team_left > span.score')[0].text
                    team_right_score = schedule.select('.team_right > span.score')[0].text
                    team_right = schedule.select('.team_right > span.name')[0].text
                    message += f"{team_left} {team_left_score} : {team_right_score} {team_right} \n"
                except IndexError:
                    try:
                        team_left = schedule.select('.team_left > span.name')[0].text
                        team_right = schedule.select('.team_right > span.name')[0].text
                        message += f"{team_left} vs {team_right} \n"
                    except IndexError:
                        pass
        today_match_list = (message.split('^'))
        return today_match_list 


    def month_match(self, league='epl'):
        naver_wfootball = f"https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=07&category={league}"
        self.driver.get(naver_wfootball)

        page = self.driver.page_source
        team_day =  BeautifulSoup(page,"html.parser")
        team_day_list = team_day.select('.schedule_month_table>table>tbody>tr')

        month_match_list = []
        message = ""
        for schedule in team_day_list:
            try:
                day = schedule.select('th > div.inner > em')[0].text
                message += f"^날짜 : {day}일\n"
            except IndexError:
                pass
            try:
                time = schedule.select('.time_place > div.inner > span.time')[0].text
                message += f"시간 : {time} "
            except IndexError:
                message += "경기가 없습니다"
            try:
                team_left = schedule.select('.team_left > span.name')[0].text
                team_left_score = schedule.select('.team_left > span.score')[0].text
                team_right_score = schedule.select('.team_right > span.score')[0].text
                team_right = schedule.select('.team_right > span.name')[0].text
                message += f"{team_left} {team_left_score} : {team_right_score} {team_right} \n"
            except IndexError:
                try:
                    team_left = schedule.select('.team_left > span.name')[0].text
                    team_right = schedule.select('.team_right > span.name')[0].text
                    message += f"{team_left} vs {team_right} \n"
                except IndexError:
                    pass
                
        month_match_list = (message.split('^'))
        return month_match_list