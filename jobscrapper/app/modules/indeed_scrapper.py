from wsgiref import headers
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
# from app import views
class scrapper:
    def __init__(self,linkee):
        self.linkin= linkee
    def indeed(self):
        # self.proxy = '71.19.249.118:8001'
        self.dict={}
        self.index=0
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'}
        self.url = f"https://pk.indeed.com/jobs?q=java&l=Karachi&pp=gQAAAAAAAAAAAAAAAAAB4rFYYwADAAABAAA&vjk=c4e98f2574d1e631"
        self.req = HTMLSession().get(self.url,headers=self.headers)
        # self.req = requests.get(self.url,headers=self.headers)
        # self.soup = BeautifulSoup(self.req.content,'html.parser')
        # self.jobs = self.soup.find_all('div',class_='cardOutline')
        self.jobs = self.req.html.find('div.cardOutline')
        for self.job in self.jobs:
            self.jobname = self.job.find('span').text
            self.company_name =  self.job.find('span',class_='companyName').text
            self.Requirment = self.job.find('div',class_='job-snippet').text
            self.job_detail={'Designation':self.jobname,'Company Name':self.company_name,'Requirment':self.Requirment,'Link':self.url}
            self.dict.update({f'Job: {self.index}':self.job_detail})
        print(f'self.linkin{self.linkin}')
        print(f'self.url{self.url}')
        print(f'self.req{self.req}')
        print(f'self.jobs{self.jobs}')
        # print(self.req.request.headers)
        # print(self.soup)
        return self.dict
# a = indeed('deed')
# print(a)