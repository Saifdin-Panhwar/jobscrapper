from urllib import request
from django.shortcuts import render
from .modules import indeed_scrapper,scrapper
from django.views import View
# Create your views here.
# url = request.('url_link')
class myclass(View):

    def get(self,request):
        print("see here")
        linkee = request.POST.get('url_link')
    # linktwo = request.POST.get('url_link')
    # print(linkee)
    # linktwo = requests.post.__get__('url_link')
        timeclass = scrapper.timesjob(linkee)
        indeed = indeed_scrapper.scrapper(linkee)
        context = timeclass.returnjobs()
        context2 = indeed.indeed()
        print(linkee)
    #     
    # print(context)
    # print(url)
    # print(context2)
        return render(request, 'app/index.html', {'context':context,'context2':context2})
    def post(self,request):
        print("see here")
        linkee = request.POST.get('url_link')
    # linktwo = request.POST.get('url_link')
    # print(linkee)
    # linktwo = requests.post.__get__('url_link')
        timeclass = scrapper.timesjob(linkee)
        indeed = indeed_scrapper.scrapper(linkee)
        context = timeclass.returnjobs()
        context2 = indeed.indeed()
        print(linkee)
    #     
    # print(context)
    # print(url)
    # print(context2)
        return render(request, 'app/index.html', {'context':context,'context2':context2})