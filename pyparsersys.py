from bs4 import BeautifulSoup
import requests
import geocoder
import time
import datetime
import pyowm
#переменные
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
EURO_RUB = 'https://www.google.ru/search?newwindow=1&source=hp&ei=OsNsX5ykCKyJrwSqppi4Ag&q=курс+евро+к+рублю&oq=курс+евро+к+рублю&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoFCAAQsQM6AgguOggIABCxAxCDAToICC4QsQMQgwE6CAgAEAoQARAqOgYIABAKEAE6BQguELEDOgYIABAKECo6BAgAEApKBQgJEgExSgYIChICMjFQ_QlY_klggUxoBXAAeACAAW6IAZ0MkgEEMjAuMZgBAKABAaoBB2d3cy13aXqwAQA&sclient=psy-ab&ved=0ahUKEwicqbevlYLsAhWsxIsKHSoTBicQ4dUDCAw&uact=5'
BITCOIN_RUB = 'https://www.google.ru/search?newwindow=1&source=hp&ei=Jbl5X7T0HOSmrgTH3afgAQ&q=биткоин+&oq=биткоин+&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyBQgAELEDMggIABCxAxCDATICCAAyAggAMgIIADICCAA6BQguELEDOggILhCxAxCDAToCCC46CggAELEDEEYQggJKBQgJEgExSgUIChIBOFDaD1jZH2DtJGgBcAB4AIABYYgB1wSSAQE4mAEAoAEBqgEHZ3dzLXdperABAA&sclient=psy-ab&ved=0ahUKEwj0mvDK8ZrsAhVkk4sKHcfuCRwQ4dUDCAc&uact=5'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}



#сам парсинг
class Dollar(object):
    headers = headers
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    var = convert[0].text
class Euro(object):
    headers = headers
    full_page = requests.get(EURO_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    var = convert[0].text
class Bitcoin(object):
    headers = headers
    full_page = requests.get(BITCOIN_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    var = convert[0].text
class Weather(object):
    g = geocoder.ip('me')
    owm = pyowm.OWM('7885a9b0a48bb719566fa5fa8986c822', language='ru')
    observation = owm.weather_at_coords(*g.latlng)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']

#тырим значения из классов и передаем их в ядро
temp = Weather.temp
w = Weather.w
bit = Bitcoin.var
dol = Dollar.var
eur = Euro.var