from asyncore import write
from operator import index
from unicodedata import name
from bs4 import BeautifulSoup
import requests
# from app import views
class timesjob:
    def __init__(self,linkee):
        self.linkin = linkee
        
#print(jobs)
        
    
    def returnjobs(self):
        self.req = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={self.linkin}&txtLocation=",'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0')
        self.soup = BeautifulSoup(self.req.content,'html.parser')
        self.jobs = self.soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        self.dict = {}
        self.index=0
        for self.job in self.jobs:
            self.index=self.index+1
            self.jobname=self.job.find('h2').text
            self.company_name=self.job.find('h3').text
            # experience=job.find('li').text.replace('card_travel','')
            self.skills=self.job.find('span',class_='srp-skills').text.replace(' ','')
            # postdate=job.find('span',class_='sim-posted').text
            self.job_link=self.job.header.h2.a['href']
            # self.job_skills=self.skills.split(",")
            self.job_detail={'Designation':self.jobname.strip(),'Company Name':self.company_name.strip(),'Skills':self.skills,'Link':self.job_link.strip}
            self.dict.update({f'Job: {self.index}':self.job_detail})
        
        return self.dict
# a= timesjob('java')
# print(a.returnjobs)
