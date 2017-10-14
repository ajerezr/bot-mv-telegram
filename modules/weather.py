from datetime import datetime, timedelta
from modules.tools import GetJson, Strip_accents
from config import getWheatApiKey
import logging
import modules.loggers
import os
import collections
import traceback

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib not available")

logger = logging.getLogger(__name__)

icondict = {'01d': ' \U00002600', '01n': ' \U0001F31B', '02d': ' \U000026C5', '02n': ' \U0001F31B' + '\U00002601',
            '03d': ' \U00002601', '03n': ' \U00002601', '04d': ' \U00002601' + '\U00002601',
            '04n': ' \U00002601' + '\U00002601', '09d': ' \U00002614' + '\U00002614',
            '09n': ' \U00002614' + '\U00002614', '10d': ' \U00002614' + '\U00002600' + '\U00002601',
            '10n': ' \U00002614' + '\U0001F31B' + '\U00002601',
            '11d': ' \U00002614' + '\U00002601' + '\U0001F4A8' + '\U000026A1',
            '11n': ' \U00002614' + '\U00002601' + '\U0001F4A8' + '\U000026A1', '13d': ' \U00002744' + '\U00002744',
            '13n': ' \U00002744' + '\U00002744', '50d': ' \U0001F301', '50n': ' \U0001F301'}

paths = {'root_dir': os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]}
paths['temp_folder'] = paths['root_dir'] + '/files/temp/'


def GetData(son):
    Data = {}
    daylist, templist, humilist, prevlist, iconlist = [], [], [], [], []
    if 'Error' in str(son['message']):
        logger.error('api response {}'.format(son['message']))
        Data['error'] = son['message']
    else:
        for data in range(len(son['list'])):
            daylist.append(datetime.strptime(son['list'][data]['dt_txt'], '%Y-%m-%d %H:%M:%S'))
            templist.append(son['list'][data]['main']['temp'])
            humilist.append(son['list'][data]['main']['humidity'])
            prevlist.append(son['list'][data]['weather'][0]['description'])
            iconlist.append(son['list'][data]['weather'][0]['icon'])
        Data['LastDate'] = datetime.strptime(son['list'][0]['dt_txt'], '%Y-%m-%d %H:%M:%S')
        Data['datetimes'] = daylist
        Data['Temps'] = templist
        Data['humidity'] = humilist
        Data['prevlist'] = prevlist
        Data['iconlist'] = iconlist
        Data['titleplot'] = [son['city']['name'], son['city']['country']]
    return Data


def format_msg(son, data):
    msg = {'name': "*" + son['city']['name'] + "," + son['city']['country'] + "*\n",
           'cords': "*Lat:*" + str(son['city']['coord']['lat']) + " " + "*long:*" + str(
               son['city']['coord']['lon']) + "\n",
           'Temp_last': "*Temp:* " + str(son['list'][0]['main']['temp']) + "º" + "\n",
           'Humi_last': "*Humidity:* " + str(son['list'][0]['main']['humidity']) + "%" + "\n",
           'Prev_last': "*Status:* " + son['list'][0]['weather'][0]['description'] + icondict[
               son['list'][0]['weather'][0]['icon']] + "\n"}
    msg['Txt_top'] = msg['name'] + msg['cords'] + msg['Temp_last'] + msg['Humi_last'] + msg['Prev_last']
    msg['full_prev'] = {'Today': '*Hoy*:\n', 'Tomorrow': '*Mañana:*\n'}
    ndates = 0
    for items in data['datetimes']:
        if items.day == data['LastDate'].day:
            msg['full_prev']['Today'] += items.strftime('%H:%M') + " " + str(data['prevlist'][ndates]) + icondict[
                data['iconlist'][ndates]] + '\n'
        elif items.day == (data['LastDate'] + timedelta(days=1)).day:
            msg['full_prev']['Tomorrow'] += items.strftime('%H:%M') + " " + str(data['prevlist'][ndates]) + icondict[
                data['iconlist'][ndates]] + '\n'
        elif items.day != (data['LastDate'] + timedelta(days=1)).day:
            date = items.strftime('%y-%m-%d')
            if date not in msg['full_prev']:
                msg['full_prev'][date] = items.strftime('*%d of %B*') + ":\n"
                msg['full_prev'][date] += items.strftime('%H:%M') + " " + str(data['prevlist'][ndates]) + icondict[
                    data['iconlist'][ndates]] + '\n'
            else:
                msg['full_prev'][date] += items.strftime('%H:%M') + " " + str(data['prevlist'][ndates]) + icondict[
                    data['iconlist'][ndates]] + '\n'
        ndates += 1
    msg['full_prev'] = collections.OrderedDict(sorted(msg['full_prev'].items()))
    msg['Txt_full_prev'] = msg['full_prev']['Today'] + msg['full_prev']['Tomorrow']
    for days in msg['full_prev']:
        if days != "Today" and days != "Tomorrow":
            msg['Txt_full_prev'] += msg['full_prev'][days]
    return msg


def PlotAll(date, temps, humi, title):
    if not plt:
        return None
    name = Strip_accents(title[0])
    plot_image = paths["temp_folder"] + name + '.png'
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)
    ax.set_frame_on(False)
    ax2 = ax.twinx()
    ax2.set_frame_on(False)
    for d in range(len(date)):
        ax.annotate(temps[d], xy=(date[d], temps[d]), xytext=(date[d], temps[d] + 0.2), fontsize=6)
    ax.fill_between(date, 0, temps, color='yellow', alpha=0.2)
    ax.plot(date, temps, linewidth=3, color='yellow', alpha=0.5)
    ax.bar(date[0], (max(temps) - min(temps)), 0.05, min(temps), facecolor='#9999ff', edgecolor='white', alpha=0.1)
    ax.annotate('<' + str(max(temps)), xy=(date[0], max(temps)), xytext=(date[0], max(temps)), color='red')
    ax.annotate('<' + str(min(temps)), xy=(date[0], min(temps)), xytext=(date[0], min(temps)), color='blue')
    ax.set_xlabel("Time (day:24h)")
    ax.set_ylabel("Temp Cº")
    lavels = []
    for dates in date:
        lavels.append(dates.strftime('%d-%H:%M'))
    ax.set_xticks(date)
    ax.set_xticklabels(lavels, fontsize=8, rotation=90)
    ax.get_xaxis().tick_bottom()
    ax2.plot(date, humi, 'b-', linewidth=2, color='blue', alpha=0.1)
    ax2.set_ylabel("Humidity %")
    ax2.get_xaxis().tick_bottom()
    plt.title(title[0] + "," + title[1], fontsize=20)
    plt.savefig(plot_image)
    plt.close(fig)
    plt.clf()
    return plot_image


def weather(query):
    ow_api = 'http://api.openweathermap.org/data/2.5/forecast/city'
    params = {'APPID': getWheatApiKey(), 'units': 'metric', 'lang': 'sp', 'q': query}
    resp = {'txt': "", 'plot': "", 'status': None, 'error': None}
    if params['APPID']:
        try:
            son = GetJson(ow_api, params)
            Data = GetData(son)
            if 'error' in Data.keys():
                resp['error'] = 'The api response: {}, try again in few seconds'.format(Data['error'])
                return resp
            else:
                msg = format_msg(son, Data)
                resp['txt'] = msg['Txt_top'] + msg['Txt_full_prev']
                resp['plot'] = PlotAll(Data['datetimes'], Data['Temps'], Data['humidity'], Data['titleplot'])
                return resp
        except Exception as error:
            resp['error'] = error
            logger.exception('error:',error)
            return resp
    else:
        resp['status'] = "Module Disabled"
        return resp
