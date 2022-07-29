from django.forms import Form
from django import forms


class HandForm(Form):

    city_id = forms.IntegerField(min_value=0, label='ID города')
    district_id = forms.IntegerField(min_value=0, label='ID района')
    street_id = forms.IntegerField(min_value=0, label='ID улицы')
    floors_cnt = forms.FloatField(min_value=0, label='Количество этажей')
    rooms_cnt = forms.FloatField(min_value=0, label='Количество комнат')
    building_year = forms.FloatField(min_value=0, label='Год постройки')
    area_total = forms.FloatField(min_value=0, label='Общая площадь')
    area_kitchen = forms.FloatField(min_value=0, label='Площадь кухни')
    series_id = forms.FloatField(min_value=0, label='Серия дома')


class ImportForm(Form):

    csv_file = forms.ImageField(widget=forms.FileInput(), label='Файл')
