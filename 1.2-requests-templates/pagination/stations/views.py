import csv
import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    df = pd.read_csv(r'C:\Users\tkaac\PycharmProjects\dj-homeworks\1.2-requests-templates\pagination\data-398-2018-08-30.csv')
    list = []
    nes_list = []
    for index, row in df.iterrows():
        d = row.to_dict()
        list.append(d)
    for i in list:
        nes_list.append({'Name': i['Name'], 'Street': i['Street'], 'District': i['District']})
    paginator = Paginator(nes_list, 10)
    page = paginator.get_page(page)
    context = {
        'bus_stations': page.nes_list,  # проверить на ноуте потом
        'page': page,
    }
    return render(request, 'stations/index.html', context)
