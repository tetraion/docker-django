
from django.views.generic import FormView, TemplateView, ListView
from requests.api import request
from requests.models import Response
from django.shortcuts import render

from .models import Fav

from . import forms

from . import scraping 

import json
import requests


class IndexView(FormView):
    form_class = forms.TextForm
    template_name = "index.html"


    
    def form_valid(self, form):
        data = form.cleaned_data
        search = data["search"]
        request = self.request

        

        if request.method == 'POST':
            if "nomal" in request.POST:
                data_rakuten = scraping.sea(search)
                total = 0
                for datum in data_rakuten:
                    total = total + datum[3]
                    
                ave_price = total/len(data_rakuten)
                ave_price = "平均価格"+str(ave_price)
            elif "min"  in request.POST:
                data_rakuten = scraping.sea_min(search)

                ave_price = data_rakuten[0][3]
                ave_price = "最安価格"+str(ave_price)
            elif "fav" in request.POST:
                # scraping.fav(request.)
                print('a')
        
        
        kekka = "楽天"


        ctxt = self.get_context_data(data_rakuten=data_rakuten, kekka="検索結果_"+kekka, form=form, ave_price=ave_price)
        return self.render_to_response(ctxt)

from django.shortcuts import redirect
class FavView(ListView):
    template_name = "fav_list.html"

    model = Fav


    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     search = data["search"]
    #     request = self.request

    # def delete_func(self, request):
    #     post_pks = self.request.POST.getlist('delete')
    #     object = Fav.objects.filter(pk__in=post_pks)
    #     context = {'object': object}
    #     if request.method == 'POST':
    #         object.delete()
    #         return redirect('app:app_list')
    #     else:
    #         return render(request, 'app/app_delete.html', context)

    def post(self,request):
        post_pks = request.POST.getlist('delete')  # <input type="checkbox" name="delete"のnameに対応
        Fav.objects.filter(pk__in=post_pks).delete()
        return redirect('fav_list')  # 一覧ページにリダイレクト
    

from django.views.generic.edit import CreateView
def abc(self):
        detum = self.request.GET
        detum=dict(detum.lists())
        detum=detum['detum']

        detum = detum[0].split(',')
        print(detum[0])
        print(detum[1])
# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    template_name = "fav_add.html"
    model = Fav
    
    fields = [ "name", "price", "url"]
    success_url = "/fav_list/"

    def get_initial(self):
        detum = self.request.GET
        detum=dict(detum.lists())
        name=detum['name']
        price=detum['price']
        url=detum['url']


        # detum = detum[0].split(',')
        initial = super().get_initial()
        initial["name"] = name[0]
        initial["price"]=price[0]
        initial["url"]=url[0]
        return initial

